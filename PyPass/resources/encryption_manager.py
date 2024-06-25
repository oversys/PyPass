import os
import base64

from cryptography.hazmat.primitives.ciphers import (
    Cipher, algorithms, modes
)

def encrypt(key, plaintext):
    iv = os.urandom(12)
    plaintext = plaintext.encode()

    encryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv),
    ).encryptor()

    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    return base64.urlsafe_b64encode(iv + ciphertext + encryptor.tag).decode()

def decrypt(key, encrypted_data):
    encrypted_data = base64.urlsafe_b64decode(encrypted_data)
    iv = encrypted_data[0:12]
    tag = encrypted_data[-16:]
    ciphertext = encrypted_data[12:-16]

    decryptor = Cipher(
        algorithms.AES(key),
        modes.GCM(iv, tag),
    ).decryptor()

    plaintext = decryptor.update(ciphertext) + decryptor.finalize() 

    return plaintext.decode() 

