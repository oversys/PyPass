import os
import json
from cryptography.fernet import Fernet

def load_db(key):
    if not os.path.exists("./resources/database.json"):
        return
    else:
        fernet = Fernet(key)

        with open("./resources/database.json", "rb") as db_file:
            encrypted_data = db_file.read()
        
        decrypted_data = json.loads(fernet.decrypt(encrypted_data).decode())

        return decrypted_data

def write_db(key, plaintext_data):
    fernet = Fernet(key)
    
    encrypted_data = fernet.encrypt(plaintext_data.encode())

    with open("./resources/database.json", "wb") as db_file:
        db_file.write(encrypted_data)
