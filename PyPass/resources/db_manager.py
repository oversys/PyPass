import os
import json
from resources.encryption_manager import *

def load_db(key):
    if not os.path.exists("./resources/database.json"):
        return
    else:
        with open("./resources/database.json", "r") as db_file:
            encrypted_data = db_file.read()
        
        decrypted_data = json.loads(decrypt(key, encrypted_data))

        return decrypted_data

def write_db(key, plaintext_data):
    encrypted_data = encrypt(key, plaintext_data)

    with open("./resources/database.json", "w") as db_file:
        db_file.write(encrypted_data)
