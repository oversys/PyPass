import os
import sys
import json
import readline
from resources.key_manager import *
from resources.db_manager import *
from resources.acc_manager import *
from resources.print_manager import print_actions, clear
from resources.update_manager import *

if not sys.stdout.isatty():
    print("The standard output of this program cannot be redirected or piped.")
    exit()

if not os.path.exists("./resources"):
    print("Resources directory missing. Please clone the full repository from oversys/PyPass.")
    exit()

key = None
try:
    key = get_key()
    valid_key = check_key(key)
    if valid_key == False:
        exit()
except KeyboardInterrupt:
    exit()

clear()

if not os.path.exists("./resources/database.json"):
    data = []
    json_data = json.dumps(data)
    write_db(key, json_data)

if os.name == "posix":
    title = """\033[38;5;39m██████\033[38;5;240m╗ \033[38;5;39m██\033[38;5;240m╗   \033[38;5;39m██\033[38;5;240m╗\033[38;5;39m██████\033[38;5;240m╗  \033[38;5;39m█████\033[38;5;240m╗ \033[38;5;39m███████\033[38;5;240m╗\033[38;5;39m███████\033[38;5;240m╗
\033[38;5;33m██\033[38;5;239m╔══\033[38;5;33m██\033[38;5;239m╗╚\033[38;5;33m██\033[38;5;239m╗ \033[38;5;33m██\033[38;5;239m╔╝\033[38;5;33m██\033[38;5;239m╔══\033[38;5;33m██\033[38;5;239m╗\033[38;5;33m██\033[38;5;239m╔══\033[38;5;33m██\033[38;5;239m╗\033[38;5;33m██\033[38;5;239m╔════╝\033[38;5;33m██\033[38;5;239m╔════╝
\033[38;5;27m██████\033[38;5;238m╔╝ ╚\033[38;5;27m████\033[38;5;238m╔╝ \033[38;5;27m██████\033[38;5;238m╔╝\033[38;5;27m███████\033[38;5;238m║\033[38;5;27m███████\033[38;5;238m╗\033[38;5;27m███████\033[38;5;238m╗
\033[38;5;26m██\033[38;5;237m╔═══╝   ╚\033[38;5;26m██\033[38;5;237m╔╝  \033[38;5;26m██\033[38;5;237m╔═══╝ \033[38;5;26m██\033[38;5;237m╔══\033[38;5;26m██\033[38;5;237m║╚════\033[38;5;26m██\033[38;5;237m║╚════\033[38;5;26m██\033[38;5;237m║
\033[38;5;25m██\033[38;5;236m║        \033[38;5;25m██\033[38;5;236m║   \033[38;5;25m██\033[38;5;236m║     \033[38;5;25m██\033[38;5;236m║  \033[38;5;25m██\033[38;5;236m║\033[38;5;25m███████\033[38;5;236m║\033[38;5;25m███████\033[38;5;236m║
\033[38;5;235m╚═╝        ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝\033[0m"""
else:
    title = """██████╗ ██╗   ██╗██████╗  █████╗ ███████╗███████╗
██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝
██████╔╝ ╚████╔╝ ██████╔╝███████║███████╗███████╗
██╔═══╝   ╚██╔╝  ██╔═══╝ ██╔══██║╚════██║╚════██║
██║        ██║   ██║     ██║  ██║███████║███████║
╚═╝        ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝"""

action = None

while action != "q":
    try:
        print(title)
        print_actions()
        action = input("Enter choice: ").lower().strip()
    except KeyboardInterrupt:
        action = "q"

    match action:
        case "1":
            try:
                clear()
                data = view_accounts(load_db(key))
                if data != None:
                    write_db(key, json.dumps(data))
                                                                                                                
                input("Press return/enter to continue...")
            except KeyboardInterrupt:
                pass
        case "2":
            try:
                clear()
                data = add_account(key, load_db(key))
                if data != None:
                    write_db(key, json.dumps(data))
            
                input("Press return/enter to continue...")
            except KeyboardInterrupt:
                pass
        case "3":
            try:
                clear()
                service = input("Service name to search: ").strip()
                specific_account(key, load_db(key), service)
                
                input("Press return/enter to continue...")
            except KeyboardInterrupt:
                pass
        case "4":
            try:
                clear()
                service = input("Service name to modify: ").strip()
                data = specific_account(key, load_db(key), service, "modify")
                if data != None:
                    write_db(key, json.dumps(data))
            
                input("Press return/enter to continue...")
            except KeyboardInterrupt:
                pass
        case "5":
            try:
                clear()
                service = input("Service name to delete: ").strip()
                data = specific_account(key, load_db(key), service, "delete")
                if data != None:
                    write_db(key, json.dumps(data))
                    
                input("Press return/enter to continue...")
            except KeyboardInterrupt:
                pass
        case "6":
            try:
                clear()
                gen_pass()
                
                input("Press return/enter to continue...")
            except KeyboardInterrupt:
                pass
        case "7":
            try:
                clear()
                update()
                
                input("Press return/enter to continue...")
            except KeyboardInterrupt:
                pass
        case "8":
            try:
                clear()

                with open("./resources/info.json", "r") as file:
                    current_version = json.load(file).get("version")

                print(title)
                print(f"Version {current_version}")
                print("By Beta_Lost")

                input("Press return/enter to continue...")
            except KeyboardInterrupt:
                pass
        case "m":
            try:
                clear()
                change_key()
                
                input("Press return/enter to continue...")
            except KeyboardInterrupt:
                pass
        case "x":
            try:
                clear()
                confirm = input("Are you sure you want to DELETE ALL DATA? This action cannot be undone! (Y/N): ").lower().strip()

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
