import requests

tags = '—' * 10

def update():
    with open("./resources/version.txt") as file:
        current_version = float(file.read())

    latest_version = float(requests.get("https://raw.githubusercontent.com/BetaLost/PyPass/master/PyPass/resources/version.txt").content.decode())

    print(f"\n{tags}\n")

    if current_version < latest_version:
        print(f"An update is currently available.\nCurrent version: {current_version}\nLatest version: {latest_version}\n")
        confirm = input("Would you like to update? (Y/N): ").lower()

        if confirm in ("y", "yes"):
            try:
                new_acc_manager = requests.get("https://raw.githubusercontent.com/BetaLost/PyPass/master/PyPass/resources/acc_manager.py").content.decode()
                new_db_manager = requests.get("https://raw.githubusercontent.com/BetaLost/PyPass/master/PyPass/resources/db_manager.py").content.decode()
                new_get_key = requests.get("https://raw.githubusercontent.com/BetaLost/PyPass/master/PyPass/resources/get_key.py").content.decode()
                new_main_file = requests.get("https://raw.githubusercontent.com/BetaLost/PyPass/master/PyPass/PyPass.py").content.decode()

                open("./resources/version.txt", "w").write(f"{latest_version}")
                open("./resources/acc_manager.py", "w").write(new_acc_manager)
                open("./resources/db_manager.py", "w").write(new_db_manager)
                open("./resources/get_key.py", "w").write(new_get_key)
                open("./PyPass.py", "w").write(new_main_file)

                print("Successfully updated PyPass!")
                print(f"\n{tags}")

                input()
                exit()
            except requests.ConnectionError:
                print("Failed to connect to the PyPass repository. Check your internet connection and try again.")
                print(f"\n{tags}\n")

        else:
            print("Cancelled update.")
            print(f"\n{tags}\n")

    else:
        print(f"Already running the latest version! (Version {current_version})")
        print(f"\n{tags}\n")
