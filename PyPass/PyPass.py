import json
import os
import getpass as gp
from cryptography.fernet import Fernet

file_to_check = None


def does_file_exist(which_file):
    global file_to_check
    if which_file == "database":
        file_to_check = "database.json"
    if which_file == "key":
        file_to_check = "key.key"

    if os.path.exists(file_to_check):
        return True
    else:
        return False


def create_key():
    # Creates master password, or key
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        # Instructions
    print(
        'Key, has been created. Check "key.key".\nInstructions:\n* Before you open the program, paste the valid key file in this directory.\n* The program will attempt to validate the key\n* If failed, the program will be terminated\n* Once the key is validated, the program will be usable\n* Remove key from this directory and hide it somewhere only you know (this is to prevent unauthorized access, the valid key is very difficult to crack, if possible anyway)\n!! DISCLAIMER: IF KEY IS LOST, YOU WILL NOT BE ABLE TO ACCESS THE DATABASE. You may open the key.key file in a text editor and save the key somewhere to re-create the key.key file.\nDO NOT SHARE THIS KEY WITH ANYONE TO AVOID UNAUTHORIZED ACCESS!')


def get_key():
    # Accesses key
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    fernet = Fernet(key)
    return fernet


def test_key():
    if does_file_exist("key") == False:
        print('Key is not in this directory. Paste key here and relaunch program to attempt to validate it.')
        input()
        exit()

    # If the key does exist in the directory, the program will attempt validate the key
    try:
        fernet = get_key()
        testing_string = 'testing string'.encode()
        testing_string = fernet.encrypt(testing_string)
        print('Valid token provided, proceeding.')
        return

    # If the key is not valid, the program will return
    except:
        print('Error: Invalid key provided.')
        input()
        exit()


def load_database_from_file():
    with open("database.json", 'rb') as database_file:
        encrypted_data = database_file.read()

    fernet = get_key()
    plaintext_data = fernet.decrypt(encrypted_data)

    with open("database_plaintext.json", 'wb') as database_file:
        database_file.write(plaintext_data)

    with open("database_plaintext.json", "rb") as database_file:
        decrypted_data = json.load(database_file)

    os.remove("database_plaintext.json")

    return decrypted_data


def write_database_to_file(plaintext_data):
    with open('database.json', 'w') as database_file:
        json.dump(plaintext_data, database_file, indent=2)

    # reload it and load into memory
    with open("database.json", 'rb') as database_file:
        data = database_file.read()

    # get the key
    fernet = get_key()

    # Encrypts database
    encrypted_database = fernet.encrypt(data)

    # Writes encrypted database
    with open("database.json", 'wb') as f:
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
        print('###########\n')

    # Attempts to print all accounts and their information
    for account in data["accounts"]:
        print(f'Website: {account.get("website")}')
        print(f'Username: {account.get("username")}')
        print(f'Password: {account.get("password")}')
        print(f'Notes: {account.get("notes")}')

        print('###########\n')

    return


notes = None


def add_account():
    global notes

    # Asking for information
    try:
        website = input('Enter website name: ')
        username = input('Enter username: ')
        password = gp.getpass('Enter password: ')
        notes = input('Enter notes (If none, type "(N)o"): ')
    except KeyboardInterrupt:
        return

    if website == '':
        print('Website cannot be empty.')
        return
    if username == '':
        print('Username cannot be empty.')
        return
    if password == '':
        print('Password cannot be empty.')
        return
    if notes == '':
        print('Notes cannot be empty. Input "n" or "No" to choose not to enter notes.')
        return

    if notes.lower() in ('n', 'no'):
        notes = 'User did not enter notes.'

    fernet = get_key()
    encrypted_password = password.encode()
    encrypted_password = fernet.encrypt(encrypted_password)
    encrypted_password = encrypted_password.decode("utf-8")

    # Loads previous data from json file
    data = load_database_from_file()

    # Append the new data
    data["accounts"].append({
        "website": website,
        "username": username,
        "password": encrypted_password,
        "notes": notes
    })

    # Then write it back to the file
    write_database_to_file(data)

    print('###########\n')
    print('Account has been successfully added to the database!')
    return


def specific_account(website, action="view"):
    data = load_database_from_file()
    website = website.lower()

    # Looping through the accounts to find the account that the user is looking for
    for account in data["accounts"]:
        if account["website"] == website:
            fernet = get_key()
            decrypted_password = account.get("password").encode()
            decrypted_password = fernet.decrypt(decrypted_password)
            decrypted_password = decrypted_password.decode("utf-8")
            print('###########')
            print('Website: ', account.get("website"))
            print('Username: ', account.get("username"))
            print('Password: ', decrypted_password)
            print('Notes: ', account.get("notes"))
            print('###########')

            if action == "delete":
                try:
                    # Confirmation
                    prompt = input('Are you sure you want to delete? This action cannot be undone(Y/N): ').lower()
                    if prompt == 'y':
                        data["accounts"].remove(account)
                        write_database_to_file(data)
                        print('Account deleted.')
                        print('###########\n')
                    else:
                        print('Operation cancelled.')
                        print('###########\n')
                except KeyboardInterrupt:
                    return

            return

    print('Account not found!')
    print('###########\n')
    return


def select_operation():
    print('\nOperations:\nA: View Accounts\nB: Add Account\nC: Delete Account\nD: Search For Account\nE: Exit\n')
    answer = 'e'
    try:
        answer = input('Input operation letter: ').lower()
    except KeyboardInterrupt:
        pass

    print('\n###########')
    if answer == 'a':
        view_accounts()
    if answer == 'b':
        add_account()
    if answer == 'c':
        website = input('Enter website name to delete: ').lower()
        specific_account(website, "delete")
    if answer == 'd':
        website = input('Enter website name to view: ').lower()
        specific_account(website)

    return answer


# Main loop

print('''
───────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─████████──████████─██████████████─██████████████─██████████████─██████████████─
─██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████░░██─████░░██──██░░████─██░░██████░░██─██░░██████░░██─██░░██████████─██░░██████████─
─██░░██──██░░██───██░░░░██░░░░██───██░░██──██░░██─██░░██──██░░██─██░░██─────────██░░██─────────
─██░░██████░░██───████░░░░░░████───██░░██████░░██─██░░██████░░██─██░░██████████─██░░██████████─
─██░░░░░░░░░░██─────████░░████─────██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██░░██████████───────██░░██───────██░░██████████─██░░██████░░██─██████████░░██─██████████░░██─
─██░░██───────────────██░░██───────██░░██─────────██░░██──██░░██─────────██░░██─────────██░░██─
─██░░██───────────────██░░██───────██░░██─────────██░░██──██░░██─██████████░░██─██████████░░██─
─██░░██───────────────██░░██───────██░░██─────────██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─
─██████───────────────██████───────██████─────────██████──██████─██████████████─██████████████─
───────────────────────────────────────────────────────────────────────────────────────────────''')

print('Loading Assets...')

if does_file_exist("database"):
    print('"database.json" file has been found.')

    if does_file_exist("key"):
        print('"key.key" file has been found')
        test_key()
    else:
        print('Key is not in this directory. Paste key here and relaunch program to attempt to validate it.')
        input()
        exit()
else:
    if does_file_exist("key") == False:
        print("Key and database do not exist. Initiating first-time setup...")
        create_key()
        test_key()
        database_structure = {
            "accounts": []
        }
        write_database_to_file(database_structure)
    else:
        print('Key is not in this directory. Paste key here and relaunch program to attempt to validate it.')
        question = input(
            'Alternatively, a new "database.json" file along with a key can be created. Do you wish to do so ( !! WARNING: ALL DATA WILL BE LOST !! )? (Y)es or (N)o?').lower()
        if question == 'y' or 'yes':
            create_key()
            test_key()
            database_structure = {
                "accounts": []
            }
            os.remove("database.json")
            write_database_to_file(database_structure)
        else:
            exit()

function_to_run = None
while function_to_run != "e":
    function_to_run = select_operation()

print("Exiting...")
