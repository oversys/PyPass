import os

if not os.path.exists("./resources"):
    print("Resources directory missing. Please clone the full repository from BetaLost/PyPass.")
    input()
    exit()

import json
from resources.get_key import get_key
from resources.db_manager import *
from resources.acc_manager import *

tags = '—' * 10

key = None
try:
    key = get_key()
except KeyboardInterrupt:
    exit()

if key != None and not os.path.exists("./resources/database.json"):
    data = {"accounts": []}
    json_data = json.dumps(data)
    write_db(key, json_data)
elif key == None:
    print("Incorrect master password..")
    input()
    exit()

title = """
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
───────────────────────────────────────────────────────────────────────────────────────────────
"""

print(title)

operation = None

while operation != "7":
    try:
        operation = input(f"\n{tags}\n1: View accounts\n2: Add account\n3: Search for account\n4: Modify account\n5: Delete account\n6: Generate random password\n7: Exit\nX: RESET DATA\n{tags}\n\nChoice: ").lower()
    except KeyboardInterrupt:
        exit() 

    if operation == "1":
        try:
            data = view_accounts(load_db(key))
            if data != None:
                write_db(key, json.dumps(data))
        except KeyboardInterrupt:
            pass
    elif operation == "2":
        try:
            data = add_account(key, load_db(key))
            if data != None:
                write_db(key, json.dumps(data))
        except KeyboardInterrupt:
            pass
    elif operation == "3":
        try:
            service = input("Service name to search: ")
            specific_account(key, load_db(key), service)
        except KeyboardInterrupt:
            pass
    elif operation == "4":
        try:
            service = input("Service name to modify: ")
            data = specific_account(key, load_db(key), service, "modify")
            if data != None:
                write_db(key, json.dumps(data))
        except KeyboardInterrupt:
            pass
    elif operation == "5":
        try:
            service = input("Service name to delete: ")
            data = specific_account(key, load_db(key), service, "delete")
            if data != None:
                write_db(key, json.dumps(data))
        except KeyboardInterrupt:
            pass
    elif operation == "6":
        try:
            gen_pass()
        except KeyboardInterrupt:
            pass
    elif operation == "x":
        try:
            confirm = input("Are you sure you want to DELETE ALL DATA? This operation cannot be undone! (Y/N): ").lower() 

            if confirm in ("y", "yes"):
                os.remove("./resources/database.json")
                os.remove("./resources/pw.json")
                
                print("All data has been deleted..")
                input()
                exit()
        except KeyboardInterrupt:
            pass

