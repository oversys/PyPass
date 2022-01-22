import os
import json
from resources.key_manager import *
from resources.db_manager import *
from resources.acc_manager import *
from resources.update import *

tags = '—' * 10

if not os.path.exists("./resources"):
    print("Resources directory missing. Please clone the full repository from BetaLost/PyPass.")
    exit()

key = None
try:
    key = get_key()
    valid_key = check_key(key)
    if valid_key == False:
        exit()
except KeyboardInterrupt:
    exit()

if not os.path.exists("./resources/database.json"):
    data = {"accounts": []}
    json_data = json.dumps(data)
    write_db(key, json_data)

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

while operation != "8":
    try:
        operation = input(f"\n{tags}\n1: View accounts\n2: Add account\n3: Search for account\n4: Modify account\n5: Delete account\n6: Generate random password\n7: Check for updates\n8: Exit\nM: Change master password\nX: RESET DATA\n{tags}\n\nChoice: ").lower()
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
    elif operation == "7":
        update()
    elif operation == "m":
        try:
            change_key()
        except KeyboardInterrupt:
            pass
    elif operation == "x":
        try:
            confirm = input("Are you sure you want to DELETE ALL DATA? This operation cannot be undone! (Y/N): ").lower() 

            if confirm in ("y", "yes"):
                os.remove("./resources/database.json")
                
                with open("./resources/info.json", "r+") as file:
                    data = json.load(file)
                    data["salt"] = None
                    file.seek(0)
                    json.dump(data, file)
                    file.truncate()

                print("All data has been deleted.")
                exit()
        except KeyboardInterrupt:
            pass

if os.name in ("nt", "dos"):
    print("\n" * 1000) 
    os.system("cls")
else:
    print("\033c", end="")
