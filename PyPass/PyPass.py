import os
import json
from resources.key_manager import *
from resources.db_manager import *
from resources.acc_manager import *
from resources.print_manager import print_actions, clear
from resources.update import *

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

action = None

while action != "q":
    try:
        print_actions()
        action = input("Enter choice: ").lower()
    except KeyboardInterrupt:
        action = "q"

    match action:
        case "1":
            try:
                clear()
                data = view_accounts(load_db(key))
                if data != None:
                    write_db(key, json.dumps(data))
            except KeyboardInterrupt:
                pass

            input("Press return/enter to continue...")
        case "2":
            try:
                clear()
                data = add_account(key, load_db(key))
                if data != None:
                    write_db(key, json.dumps(data))
            except KeyboardInterrupt:
                pass

            input("Press return/enter to continue...")
        case "3":
            try:
                clear()
                service = input("Service name to search: ")
                specific_account(key, load_db(key), service)
            except KeyboardInterrupt:
                pass

            input("Press return/enter to continue...")
        case "4":
            try:
                clear()
                service = input("Service name to modify: ")
                data = specific_account(key, load_db(key), service, "modify")
                if data != None:
                    write_db(key, json.dumps(data))
            except KeyboardInterrupt:
                pass

            input("Press return/enter to continue...")
        case "5":
            try:
                clear()
                service = input("Service name to delete: ")
                data = specific_account(key, load_db(key), service, "delete")
                if data != None:
                    write_db(key, json.dumps(data))
            except KeyboardInterrupt:
                pass

            input("Press return/enter to continue...")
        case "6":
            try:
                clear()
                gen_pass()
            except KeyboardInterrupt:
                pass

            input("Press return/enter to continue...")
        case "7":
            clear()
            update()
            input("Press return/enter to continue...")
        case "m":
            try:
                clear()
                change_key()
            except KeyboardInterrupt:
                pass

            input("Press return/enter to continue...")
        case "x":
            try:
                clear()
                confirm = input("Are you sure you want to DELETE ALL DATA? This action cannot be undone! (Y/N): ").lower() 

                if confirm in ("y", "yes"):
                    os.remove("./resources/database.json")
                    
                    with open("./resources/info.json", "r+") as file:
                        data = json.load(file)
                        data["salt"] = None
                        file.seek(0)
                        json.dump(data, file)
                        file.truncate()

                    print("All data has been deleted.")
                    input("Press return/enter to continue...")
                    action = "q"
            except KeyboardInterrupt:
                pass

    clear()

clear()
