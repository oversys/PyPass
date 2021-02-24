import os
import json
import string
import secrets
import pyperclip
import getpass as gp
from shutil import move
from urllib.request import urlopen
from cryptography.fernet import Fernet
from tkinter import filedialog
from tkinter import Tk

if not os.path.exists("./Assets"):
        os.mkdir("./Assets")

if os.path.exists("database.json"):
    move("database.json", "Assets")

file_to_check = None
fernet = None
tags = '—' * 10


def does_file_exist(which_file):
    global file_to_check
    if which_file == "database":
        file_to_check = "./Assets/database.json"
    if which_file == "key":
        file_to_check = "key.key"

    if os.path.exists(file_to_check):
        return True
    else:
        return False


def create_key():
    global fernet
    # Creates master password, or key
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        # Instructions
    print('Key, has been created. Check "key.key".\nInstructions:\n* (Optional) If you wish to have "copy to clipboard" features then run pip install pyperclip in your terminal.\n* On first time use, a database.json file will be generated along with a key.key file. DO NOT LOSE ANY OF THOSE FILES.\n* Make sure to hide the key.key file somewhere secure, you will be prompted to browse for the file and open it when you open the program.')

    fernet = Fernet(key)


def get_key():
    # Accesses key
    global fernet
    Tk().withdraw()
    filename = filedialog.askopenfilename(title="Select key file", filetypes=[("Key Files", "*.key")])
    with open(filename, "rb") as key_file:
        key = key_file.read()
    
    fernet = Fernet(key)


def test_key():
    try:
        testing_string = 'testing string'.encode()
        testing_string = fernet.encrypt(testing_string)
        print('Valid token provided, proceeding...')
        return

    # If the key is not valid, the program will return
    except:
        print('Error: Invalid key provided.')
        input()
        exit()


def load_database_from_file():
    with open("./Assets/database.json", 'rb') as database_file:
        encrypted_data = database_file.read()

    plaintext_data = fernet.decrypt(encrypted_data)

    with open("database_plaintext.json", 'wb') as database_file:
        database_file.write(plaintext_data)

    with open("database_plaintext.json", "rb") as database_file:
        decrypted_data = json.load(database_file)

    os.remove("database_plaintext.json")

    return decrypted_data


def write_database_to_file(plaintext_data):
    with open("./Assets/database.json", 'w') as database_file:
        json.dump(plaintext_data, database_file, indent=2)

    # reload it and load into memory
    with open("./Assets/database.json", 'rb') as database_file:
        data = database_file.read()

    # Encrypts database
    encrypted_database = fernet.encrypt(data)

    # Writes encrypted database
    with open("./Assets/database.json", 'wb') as f:
        f.write(encrypted_database)

    return


def view_accounts():
    # Loads database
    data = load_database_from_file()

    number_of_accounts_loaded = len(data.get("accounts"))

    if number_of_accounts_loaded == 0:
        print('No accounts found...')
        return
    else:
        print(f'{str(number_of_accounts_loaded)} account(s) found!')
        print(f'{tags}\n')

    # Attempts to print all accounts and their information
    for account in data["accounts"]:
        print(f'Service: {account.get("website")}')
        print(f'Username: {account.get("username")}')
        print(f'Password: {account.get("password")}')
        print(f'Notes: {account.get("notes")}')

        print(f'{tags}\n')

    return


def generate_password(length):
    alphabet = string.ascii_letters + string.digits + '!@#$%^&*?'
    generated_password = ''.join(secrets.choice(alphabet) for i in range(length))
    return generated_password


notes = None
password = None


def add_account():
    global notes
    global password

    # Loads previous data from json file
    data = load_database_from_file()

    # Asking for information
    try:
        # Website/Service Name
        website = input('Enter service name: ')
        if website == '':
            print('Service name cannot be empty.')
            return
        
        for account in data["accounts"]:
            if account["website"].lower() == website.lower():
                print('Service already exists in database!')
                return
        
        # Username
        username = input('Enter username: ')
        if username == '':
            print('Username cannot be empty.')
            return
        
        # Password prompt to select
        password_prompt = input('Type "A" to Enter Password or "B" to Generate Password: ').lower()

        # User-made password
        if password_prompt == 'a':

            # Asking for password
            password = gp.getpass('Enter password: ')
            if password == '':
                print('Password cannot be empty.')
                return
            
            # Confirming password
            confirm_password = gp.getpass('Confirm password: ')
            if password != confirm_password:
                print('Passwords do not match.')
                return
        
        # Randomly generated password
        elif password_prompt == 'b':
            accepted = None
            while accepted != 'y':
                print(f'\n{tags}\n')
                print('Press CTRL + C to return to the main menu.')

                # Asking for length
                length = input('Length of new password: ')

                # Converting length to integer
                try:
                    length = int(length)
                except:
                    print('Did not enter integer.')
                    return

                # Filtering short password
                if length < 8:
                    print('Password too short, minimum characters are 8.')
                else:

                    # Generating password
                    generated_password = generate_password(length)

                    # Confirming password choice
                    print(f'Generated Password: {generated_password}')
                    confirm = input('Proceed? (Y)es or (N)o: ').lower()

                    # Handling confirm prompt
                    if confirm in ('y', 'yes'):

                        # Defining password and exiting loop
                        password = generated_password
                        try:
                            pyperclip.copy(password)
                            print('Password copied to clipboard!')
                        except:
                            print('"pyperclip" library not found, failed to copy password to clipboard.')
                        accepted = 'y'

                    # Invalid choice
                    elif confirm not in ('n', 'no'):
                        print('Invalid choice, returning to main menu.')
                        return

        # Notes
        notes = input('Enter notes (If none, type "(N)o"): ')
        if notes == '':
            print('Notes cannot be empty. Input "n" or "No" to choose not to enter notes.')
            return
        if notes.lower() in ('n', 'no'):
            notes = 'User did not enter notes.'

        # Collected Information, handling Keyboard Interrupts
    except KeyboardInterrupt:
        return
    
    encrypted_password = password.encode()
    encrypted_password = fernet.encrypt(encrypted_password)
    encrypted_password = encrypted_password.decode("utf-8")

    # Append the new data
    data["accounts"].append({
        "website": website,
        "username": username,
        "password": encrypted_password,
        "notes": notes
    })

    # Then write it back to the file
    write_database_to_file(data)

    print(f'{tags}\n')
    print('Account has been successfully added to the database!')
    return


def specific_account(website, action="view"):
    data = load_database_from_file()
    website = website.lower()

    # Looping through the accounts to find the account that the user is looking for
    for account in data["accounts"]:
        if account["website"].lower() == website:
            decrypted_password = account.get("password").encode()
            decrypted_password = fernet.decrypt(decrypted_password)
            decrypted_password = decrypted_password.decode("utf-8")
            print(tags)
            print('Service: ', account.get("website"))
            print('Username: ', account.get("username"))
            print('Password: ', decrypted_password)
            print('Notes: ', account.get("notes"))
            print(tags)

            if action == "delete":
                try:
                    # Confirmation
                    prompt = input('Are you sure you want to delete? This action cannot be undone(Y/N): ').lower()
                    if prompt == 'y':
                        data["accounts"].remove(account)
                        write_database_to_file(data)
                        print('Account deleted.')
                        print(f'{tags}\n')
                    else:
                        print('Operation cancelled.')
                        print(f'{tags}\n')
                except KeyboardInterrupt:
                    return
            elif action == "modify":
                try:
                    print('Available modifications:\nA: Username\nB: Password\nC: Notes\nD: Cancel')
                    print(f'{tags}\n')

                    # Confirmation
                    prompt = input('Enter detail to modify: ').lower()
                    if prompt == 'a':
                        new_username = input('Enter new username: ')
                        if new_username != account.get("username"):
                            if new_username == '':
                                print('New username may not be empty.')
                                return
                            
                            account["username"] = new_username
                            write_database_to_file(data)
                            print('Account modified successfully!')
                            print(f'{tags}\n')
                        else:
                            print(f'{tags}')
                            print('Usernames may not match.')
                            print(f'{tags}\n')
                            return
                    if prompt == 'b':
                        # Password prompt to select
                        password_prompt = input('Type "A" to Enter Password or "B" to Generate Password: ').lower()

                        # User-made password
                        if password_prompt == 'a':
                        
                            # Asking for password
                            new_password = gp.getpass('Enter new password: ')
                            if new_password == '':
                                print('Password cannot be empty.')
                                return

                            # Confirming password
                            confirm_password = gp.getpass('Confirm password: ')
                            if new_password != confirm_password:
                                print('Passwords do not match.')
                                return

                        # Randomly generated password
                        elif password_prompt == 'b':
                            accepted = None
                            while accepted != 'y':
                                print(f'\n{tags}\n')
                                print('Press CTRL + C to return to the main menu.')

                                # Asking for length
                                length = input('Length of new password: ')

                                # Converting length to integer
                                try:
                                    length = int(length)
                                except:
                                    print('Did not enter integer.')
                                    return

                                # Filtering short password
                                if length < 8:
                                    print('Password too short, minimum characters are 8.')
                                else:
                                
                                    # Generating password
                                    generated_password = generate_password(length)

                                    # Confirming password choice
                                    print(f'Generated Password: {generated_password}')
                                    confirm = input('Proceed? (Y)es or (N)o: ').lower()

                                    # Handling confirm prompt
                                    if confirm in ('y', 'yes'):
                                    
                                        # Defining password and exiting loop
                                        new_password = generated_password
                                        try:
                                            pyperclip.copy(new_password)
                                            print('Password copied to clipboard!')
                                        except:
                                            print('"pyperclip" library not found, failed to copy password to clipboard.')
                                        accepted = 'y'

                                    # Invalid choice
                                    elif confirm not in ('n', 'no'):
                                        print('Invalid choice, returning to main menu.')
                                        return
                            
                            encrypted_password = new_password.encode()
                            encrypted_password = fernet.encrypt(encrypted_password)
                            encrypted_password = encrypted_password.decode("utf-8")
                            account["password"] = encrypted_password
                            write_database_to_file(data)
                            print('Account modified successfully!')
                            print(f'{tags}\n')
                        else:
                            print(f'{tags}')
                            print('Passwords may not match.')
                            print(f'{tags}\n')
                            return
                    if prompt == 'c':
                        new_notes = input('Enter new notes: ')
                        if new_notes != account.get("notes"):
                            if new_notes == '':
                                print('New notes may not be empty.')
                                return
                            
                            account["notes"] = new_notes
                            write_database_to_file(data)
                            print('Account modified successfully!')
                            print(f'{tags}\n')
                        else:
                            print(f'{tags}')
                            print('Notes may not match.')
                            print(f'{tags}\n')
                            return
                    else:
                        print('Operation cancelled.')
                        print(f'{tags}\n')
                except KeyboardInterrupt:
                    return
            else:
                try:
                    pyperclip.copy(decrypted_password)
                    print('Password copied to clipboard!')
                except:
                    print('"pyperclip" library not found, failed to copy password to clipboard.')

            return

    print('Account not found!')
    print(f'{tags}\n')
    return


def select_operation():
    print('\nOperations:\nA: View Accounts\nB: Add Account\nC: Delete Account\nD: Search For Account\nE: Modify Account\nX: Reset Data\nF: Exit\n')
    answer = 'e'
    try:
        answer = input('Input operation letter: ').lower()
    except KeyboardInterrupt:
        exit()

    print(f'\n{tags}')
    if answer == 'a':
        view_accounts()
    elif answer == 'b':
        add_account()
    elif answer == 'c':
        try:
            website = input('Enter service name to delete: ').lower()
        except KeyboardInterrupt:
            return
        specific_account(website, "delete")
    elif answer == 'd':
        try:
           website = input('Enter service name to view: ').lower()
        except KeyboardInterrupt:
            return
        specific_account(website)
    elif answer == 'e':
        try:
           website = input('Enter service name to modify: ').lower()
        except KeyboardInterrupt:
            return
        specific_account(website, "modify")
    elif answer == 'x':
        question = input('Are you sure you want to delete ALL data? (Y)es or (N)o: ').lower()
        if question in ('y', 'yes'):
            filename = filedialog.askopenfilename(title="Select key file", filetypes=[("Key Files", "*.key")])
            os.remove(filename)
            os.remove("./Assets/database.json")
        else:
            return

    return answer


# Main loop

try:
    with open('./Assets/text.txt', 'r', encoding='utf-8') as text_file:
        print(text_file.read())
except:
    try:
        requested_text = urlopen("https://raw.githubusercontent.com/BetaLost/PyPass/master/PyPass/Assets/text.txt")

        with open("./Assets/text.txt", 'w', encoding='utf-8') as text_file:    
            for line in requested_text:
                text_file.write(f'{line.decode().strip()}\n')
        
        with open("./Assets/text.txt", 'r', encoding='utf-8') as text_file:
            print(text_file.read())
    except:
        print('"Assets/text.txt" file not found. Failed to retrieve file from GitHub repo. A re-attempt will be done when launching program next time.')


print('Loading Assets...')

if does_file_exist("database"):
    print('"database.json" file has been found.')

else:
    print("Database does not exist. Initiating first-time setup...")
    create_key()
    database_structure = {
        "accounts": []
    }
    write_database_to_file(database_structure)

if fernet is None:
    try:
        get_key()
        print('"key.key" file has been found.')
    except:
        print('Failed to access "key.key" file.')
        input()
    exit()

function_to_run = None
while function_to_run != "f":
    function_to_run = select_operation()

print("Exiting...")
