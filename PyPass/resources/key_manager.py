import os
import json
import base64
import getpass as gp
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from resources.db_manager import load_db

def get_key():
    master_pass = gp.getpass("Master password: ").encode()
    salt = None

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
            iterations=100000
            )

        key = kdf.derive(master_pass)

        return key

def check_key(key):
    try:
        load_db(key)
    except:
        print("Incorrect master password..")
        exit()

