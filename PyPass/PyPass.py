import json
import os.path
from cryptography.fernet import Fernet
import atexit
import getpass as gp


def check_assets():
    # Check if "database.json" exists
    if os.path.exists("database.json"):
        print('Database has been loaded...')

    # If not, it will create it
    else:
        file = open("database.json", 'w')
        file.write('''{
  "accounts": [
    
  ]
}''')
        file.close()
        print('"database.json" has been created...')
        create_master_password()


def create_master_password():
    # Creates master password, or key
    key = Fernet.generate_key()
    file = open("key.key", 'wb')
    file.write(key)
    file.close()

    # Instructions
    print('Master password, or key, has been created. Check "key.key".\nInstructions:\n* Before you open the program, paste the valid key in this directory.\n* The program will attempt to validate the key\n* If failed, the program will be terminated\n* Once the key is validated, the database will be unlocked, or decrypted\n* When you exit the program, the database will be automatically locked, or encrypted\n* Remove key from this directory and hide it somewhere only you know (this is to prevent unauthorized access, the valid key is very difficult to crack, if possible anyway)\n!! DISCLAIMER: IF KEY IS LOST, YOU WILL NOT BE ABLE TO ACCESS THE DATABASE. You make open the key.key file in a text editor and save the key somewhere to re-create the key.key file.\nDO NOT SHARE THIS KEY WITH ANYONE TO AVOID UNAUTHORIZED ACCESS!')


def read_key():
    # Check if "key.key" file exists
    if os.path.exists("key.key"):
        file = open("key.key", 'rb')
        key = file.read()
        file.close()

        # If the key does exist in the directory, the program will attempt validate the key
        try:
            fernet = Fernet(key)
            testing_string = 'testing string'.encode()
            testing_string = fernet.encrypt(testing_string)
            print('Valid token provided, proceeding.')

        # If the key is not valid, the program will be terminated
        except:
            print('Error: Invalid key provided.')
            input()
            exit()

    # Key not found prompt
    else:
        print('Key not found. Paste the valid "key.key" file in this directory to unlock the program.\nNote: If you have the key but deleted the key.key file, create a new file with the name "key" and extension ".key" so that it becomes a "key.key" file. Open the file with a text editor and paste your key inside the file.\nIf you completely lost your key, you are unable to unlock this database, therefore, you make delete the "database.json" file to start a new database. A new key will be generated if you do.\nIF YOU DELETE THE CURRENT DATABASE, ALL ENTRIES WILL BE LOST!')
        input()
        exit()


def encrypt_database():
    # Reads decrypted version of "database.json"
    with open("database.json", 'rb') as f:
        data = f.read()

    # Accesses key
    file = open("key.key", 'rb')
    key = file.read()
    file.close()
    fernet = Fernet(key)

    # Encrypts database
    encrypted_database = fernet.encrypt(data)

    # Writes encrypted database
    with open("database.json", 'wb') as f:
        f.write(encrypted_database)


def decrypt_database():
    # Reads encrypted version of "database.json
    with open("database.json", 'rb') as f:
        data = f.read()

    # Accesses key
    file = open("key.key", 'rb')
    key = file.read()
    file.close()
    fernet = Fernet(key)

    # Decrypts database
    decrypted_database = fernet.decrypt(data)

    # Writes decrypted database
    with open("database.json", 'wb') as f:
        f.write(decrypted_database)


def view_accounts():
    # Loads "database.json"
    with open("database.json", 'r') as f:
        data = json.load(f)

    # Attempts to print all accounts and their information
    try:
        for account in data['accounts']:
            print(f'Website: {account["website"]}')
            print(f'Username: {account["username"]}')
            print(f'Password: {account["password"]}')
            print(f'Notes: {account["notes"]}')
            print('###########\n')
    except:
        print('###########\n')
        print('No accounts found!')

    select_operation()


def add_account():
    # Asking for information
    website = input('Enter website name: ').lower()
    username = input('Enter username: ')
    password = gp.getpass('Enter password: ')
    notes = input('Enter notes (If none, type "None"): ')

    # Accesses key
    file = open("key.key", 'rb')
    key = file.read()
    file.close()
    fernet = Fernet(key)

    # Encrypting Password
    password = password.encode()
    encrypted_password = fernet.encrypt(password)
    encrypted_password = encrypted_password.decode("utf-8")

    # Prepares to add new account
    new_account = {"website": website, "username": username, "password": encrypted_password, "notes": notes}

    # Loads "database.json"
    with open("database.json", 'r+') as file:
        data = json.load(file)

        # Adding the new account to the database
        data["accounts"].append(new_account)
        file.seek(0)
        json.dump(data, file, indent=2)

    print('###########\n')
    print('Account has been successfully created!')
    select_operation()


def delete_account():
    # Asking for account website
    website = input('Enter website name: ').lower()
    with open("database.json") as f:
        data = json.load(f)

    # Looping through the accounts to find the account that the user is looking for
    for account in data["accounts"]:
        if account["website"] == website:
            print('###########')
            print(f'Website: {account["website"]}')
            print(f'Username: {account["username"]}')
            print(f'Password: {account["password"]}')
            print(f'Notes: {account["notes"]}')
            print('###########')

            # Confirmation
            prompt = input('Are you sure you want to delete? This action cannot be undone(Y/N): ').lower()
            if prompt == 'y':
                data["accounts"].remove(account)
                with open("database.json", 'w') as f:
                    json.dump(data, f, indent=2)
                print('Account deleted.')
                print('###########\n')
                select_operation()
                return
            else:
                print('Operation cancelled.')
                print('###########\n')
                select_operation()
                return

    print('###########\n')
    print('Account not found!')
    select_operation()


def search_for_account():
    # Asking for account website
    website = input('Enter website name: ').lower()
    with open("database.json") as f:
        data = json.load(f)

    # Accesses key
    file = open("key.key", 'rb')
    key = file.read()
    file.close()
    fernet = Fernet(key)

    # Looping through the accounts to find the account that the user is looking for
    for account in data["accounts"]:
        if account["website"] == website:
            decrypted_password = account["password"].encode()
            decrypted_password = fernet.decrypt(decrypted_password)
            print('###########')
            print(f'Website: {account["website"]}')
            print(f'Username: {account["username"]}')
            print(f'Password - Encrypted: {account["password"]}')
            print(f'Password - Decrypted: {decrypted_password}')
            print(f'Notes: {account["notes"]}')
            print('###########')

            select_operation()
            return

    print('Account not found!')
    print('###########\n')
    select_operation()


def select_operation():
    print('\nOperations:\nA: View Accounts\nB: Add Account\nC: Delete Account\nD: Search For Account\nE: Exit\n')
    answer = 'e'
    try:
        answer = input('Input operation letter: ').lower()
    except:
        encrypt_database()

    print('\n###########')
    if answer == 'a':
        view_accounts()
    elif answer == 'b':
        add_account()
    elif answer == 'c':
        delete_account()
    elif answer == 'd':
        search_for_account()
    else:
        exit()


print('Loading Assets...')
check_assets()

print('Reading key.key file...')
read_key()
try:
    decrypt_database()
except:
    pass

print('\n################')
print('PyPass unlocked!')
print('################\n')

select_operation()

atexit.register(encrypt_database)
