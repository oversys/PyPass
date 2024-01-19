import os
import json
import base64
import getpass as gp
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from resources.db_manager import *
from resources.encryption_manager import *

def get_key(mode=None):
    
    if mode == "change":
        master_pass = gp.getpass("New master password: ").encode()
        confirm_master_pass = gp.getpass("Confirm new master password: ").encode()
        if master_pass != confirm_master_pass:
            print("Passwords do not match.")
            return
    elif mode == "pre_change":
        master_pass = gp.getpass("Current master password: ").encode()
    elif os.path.exists("./resources/database.json"):
        master_pass = gp.getpass("Master password: ").encode()
    else:
        master_pass = gp.getpass("Set master password (first time setup): ").encode()
        confirm_master_pass = gp.getpass("Confirm master password (first time setup): ").encode()
        
        if master_pass != confirm_master_pass:
            print("Passwords do not match.")
            exit()

    with open("./resources/info.json", "r+") as file:
        data = json.load(file)

        salt = data.get("salt")

        if salt != None:
            salt = base64.urlsafe_b64decode(salt.encode())
        else:
            salt = os.urandom(16)
            data["salt"] = base64.urlsafe_b64encode(salt).decode()
            file.seek(0)
            json.dump(data, file)
            file.truncate()

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA512(),
            length=32,
            salt=salt,
            iterations=120000
            )

        key = kdf.derive(master_pass)

        return key

def check_key(key):
    try:
        load_db(key)
    except:
        print("Incorrect master password..")
        return False

def change_key():
    key = get_key("pre_change")
    valid_key = check_key(key)
    if valid_key == False:
        return

    new_key = get_key("change")
    if new_key == None:
        return

    data = load_db(key)

    for account in data:
        decrypted_password = decrypt(key, account.get("password"))
        new_password = encrypt(new_key, decrypted_password)
        account["password"] = new_password

    write_db(new_key, json.dumps(data))
    print("\nSuccessfully changed master password!")
    exit()
