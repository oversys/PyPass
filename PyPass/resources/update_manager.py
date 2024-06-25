import json
import requests

tags = '—' * 10

def update():
    base_link = "https://raw.githubusercontent.com/oversys/PyPass/main/PyPass"

    with open("./resources/info.json", "r") as file:
        current_version = json.load(file).get("version")

    latest_version = json.loads(requests.get(f"{base_link}/resources/info.json").content.decode()).get("version")

    print(f"\n{tags}\n")

    if current_version < latest_version:
        print(f"An update is currently available.\nCurrent version: {current_version}\nLatest version: {latest_version}\n")
        confirm = input("Would you like to update? (Y/N): ").lower().strip()

        if confirm in ("y", "yes"):
            try:
                new_encryption_manager = requests.get(f"{base_link}/resources/encryption_manager.py").content.decode()
                new_key_manager = requests.get(f"{base_link}/resources/key_manager.py").content.decode()
                new_acc_manager = requests.get(f"{base_link}/resources/acc_manager.py").content.decode()
                new_db_manager = requests.get(f"{base_link}/resources/db_manager.py").content.decode()
                new_print_manager = requests.get(f"{base_link}/resources/print_manager.py").content.decode()
                new_update_manager = requests.get(f"{base_link}/resources/update_manager.py").content.decode()
                new_main_file = requests.get(f"{base_link}/PyPass.py").content.decode()

                open("./resources/encryption_manager.py", "w").write(new_encryption_manager)
                open("./resources/key_manager.py", "w").write(new_key_manager)
                open("./resources/acc_manager.py", "w").write(new_acc_manager)
                open("./resources/db_manager.py", "w").write(new_db_manager)
                open("./resources/print_manager.py", "w").write(new_print_manager)
                open("./resources/update_manager.py", "w").write(new_update_manager)
                open("./PyPass.py", "w").write(new_main_file)

                with open("./resources/info.json", "r+") as file:
                    data = json.load(file)
                    data["version"] = latest_version
                    file.seek(0)
                    json.dump(data, file)
                    file.truncate()

                print("Successfully updated PyPass!")
                exit()
            except requests.ConnectionError:
                print("Failed to connect to the PyPass repository. Check your internet connection and try again.")
                print(f"\n{tags}\n")

        else:
            print("Cancelled update.")
            print(f"\n{tags}\n")

    else:
        print(f"Already running the latest version! (Version {current_version})")
        print(f"{tags}\n")
