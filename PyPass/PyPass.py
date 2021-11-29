import os
import json
from resources.get_key import get_key
from resources.db_manager import *
from resources.acc_manager import *

tags = '—' * 10

if not os.path.exists("./resources"):
    print("Resources directory missing. Please clone the full repository from BetaLost/PyPass.")

key = get_key()

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
    operation = input(f"\n{tags}\n1: View accounts\n2: Add account\n3: Search for account\n4: Modify account\n5: Delete account\n6: Generate random password\n7: Exit\nX: RESET DATA\n{tags}\n\nChoice: ").lower()

    if operation == "1":
        data = view_accounts(load_db(key))
        if data != None:
            write_db(key, json.dumps(data))
    elif operation == "2":
        data = add_account(key, load_db(key))
        if data != None:
            write_db(key, json.dumps(data))
    elif operation == "3":
        service = input("Service name to search: ")
        specific_account(key, load_db(key), service)
    elif operation == "4":
        service = input("Service name to modify: ")
        data = specific_account(key, load_db(key), service, "modify")
        if data != None:
            write_db(key, json.dumps(data))
    elif operation == "5":
        service = input("Service name to delete: ")
        data = specific_account(key, load_db(key), service, "delete")
        if data != None:
            write_db(key, json.dumps(data))
    elif operation == "6":
        gen_pass()
    elif operation == "x":
        confirm = input("Are you sure you want to DELETE ALL DATA? This operation cannot be undone! (Y/N): ").lower() 

        if confirm in ("y", "yes"):
            os.remove("./resources/database.json")
            os.remove("./resources/pw.json")
            
            print("All data has been deleted..")
            input()
            exit()
