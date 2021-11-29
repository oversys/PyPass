import os
import json
import base64
import getpass as gp
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def get_key():
    master_pass = gp.getpass("Master password: ").encode()
    
    salt = None
    key = None

    if os.path.exists("./resources/pw.json"):
        with open("./resources/pw.json", "r") as file:
            data = json.load(file)
            salt = base64.urlsafe_b64decode(data.get("salt"))
            master_hash = data.get("masterHash").encode()

        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000
            ) 
        key = base64.urlsafe_b64encode(kdf.derive(master_pass))

        if master_hash == key:
            return key
        else:
            return

    else:
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000
            )
        key = base64.urlsafe_b64encode(kdf.derive(master_pass)).decode("utf-8")
        salt = base64.urlsafe_b64encode(salt).decode("utf-8")
        
        with open("./resources/pw.json", "w") as file:
            data = {"masterHash": key, "salt": salt}
            json.dump(data, file)

        return key
