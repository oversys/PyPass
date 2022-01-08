import string
import secrets
import time
import getpass as gp
from cryptography.fernet import Fernet

try:
    import pyperclip
except:
    print("Could not import pyperclip module.")

tags = '—' * 10


def gen_pass():
    alphabet = string.ascii_letters + string.digits + '!@#$%^&*?'
    accepted = None

    while accepted != "y":
        print(f"\n{tags}\n")

        length = input("Password length: ")

        try:
            length = int(length)
        except:
            print("Did not enter an integer.")
            return

        generated_password = ''.join(secrets.choice(alphabet)
                                     for i in range(length))

        print(f"Generated password: {generated_password}")
        confirm = input("Accept password? (Y/N): ").lower()

        if confirm in ("y", "yes"):
            try:
                pyperclip.copy(generated_password)
                print("Password copied to clipboard!")
            except pyperclip.PyperclipException:
                print("Pyperclip requires the \"xclip\" package to be installed on Linux systems. Please install it to make use of the copy-to-clipboard features.")
            except:
                print("\"Pyperclip\" library not found, failed to copy password to clipboard.")
            
            accepted = "y"
            return generated_password

        elif confirm not in ("n", "no"):
            print("Invalid choice.")
            return

def view_accounts(data):
    total_accounts = len(data.get("accounts"))

    if total_accounts == 0:
        print(f"\n{tags}\nNo accounts found.\n{tags}\n")
        return
    elif total_accounts == 1:
        print(f"\n{tags}\n{str(total_accounts)} account found!\n{tags}\n")
    else:
        print(f"\n{tags}\n{str(total_accounts)} accounts found!\n{tags}\n")

    for account in data.get("accounts"):
        print(f"Service: {account.get('service')}")
        print(f"Username: {account.get('username')}")
        print(f"Password: {account.get('password')}")
        print(f"Notes: {account.get('notes')}")

        print(f"\n{tags}\n")
    
    return

def add_account(key, data):
    password = None
    notes = None
    fernet = Fernet(key)

    service = input("Enter service name: ")

    for account in data.get("accounts"):
        if account.get("service").lower() == service.lower():
            print("Service already exists in database!")
            return

    if service == '':
        print("Service name cannot be empty.")
        return

    username = input("Enter username: ")

    if username == '':
        print("Username name cannot be empty.")
        return

    password_prompt = input(f"\n{tags}\n1: Enter password\n2: Generate password\n3: Cancel\n{tags}\n\nChoice: ").lower()

    if password_prompt == "1":
        password = gp.getpass('Enter password: ')

        if password == '':
            print('Password cannot be empty.')
            return
            
        confirm_password = gp.getpass('Confirm password: ')

        if password != confirm_password:
            print('Passwords do not match.')
            return
    
    elif password_prompt == "2":
        password = gen_pass()
        
        if password == None:
            return

    else:
        return

    notes = input("Enter notes (Leave empty for no notes): ")

    if notes == "":
        notes = "User did not enter notes."

    encrypted_password = fernet.encrypt(password.encode())

    data.get("accounts").append({
        "service": service,
        "username": username,
        "password": encrypted_password.decode("utf-8"),
        "notes": notes
        })

    print(f"{tags}\n")
    print("Account has been added to the database.")
    return data

def specific_account(key, data, service, action="view"):
    service = service.lower()
    fernet = Fernet(key)

    for account in data.get("accounts"):
        if account.get("service").lower() == service:
            decrypted_password = fernet.decrypt(account.get("password").encode()).decode("utf-8")

            print(f"\n{tags}")
            print(f"Service: {account.get('service')}")
            print(f"Username: {account.get('username')}")
            print(f"Notes: {account.get('notes')}")

            try: 
                for i in range(-15, 0):
                    print(f"Password: {decrypted_password} (Removing in {abs(i)} seconds, press CTRL+C to skip.)", end="\r")
                    time.sleep(1)
                    print(" " * 99, end="\r")
            except KeyboardInterrupt:
                pass

            print(" " * 99, end="\r")
            print("Password: ********")
            print(f"{tags}\n")

            confirm = input("Would you like to copy the password to clipboard? (Y/N): ").lower()

            if confirm in ("y", "yes"):
                try:
                    pyperclip.copy(decrypted_password)
                    print("Password copied to clipboard!")
                except pyperclip.PyperclipException:
                    print("Pyperclip requires the \"xclip\" package to be installed on Linux systems. Please install it to make use of the copy-to-clipboard features.")
                except:
                    print("\"Pyperclip\" library not found, failed to copy password to clipboard.")

            if action == "delete":
                confirm = input("Are you sure you want to delete this account entry? This action cannot be undone (Y/N): ").lower()

                if confirm in ("y", "yes"):
                    data.get("accounts").remove(account)
                    print("Account deleted.")
                    return data
            elif action == "modify":
                modify_prompt = input(f"\n{tags}\n1: Change username\n2: Change password\n3: Change notes\n4: Cancel\n{tags}\n\nChoice: ").lower()

                if modify_prompt == "1":
                    new_username = input("Enter new username: ")

                    if new_username == "":
                        print("New username may not be empty.")
                        return
                    elif new_username != account.get("username"):
                        account["username"] = new_username
                        print("Successfully changed username!")
                        return data

                elif modify_prompt == "2":
                    new_password = None
                    password_prompt = input(f"\n{tags}\n1: Enter password\n2: Generate password\n3: Cancel\n{tags}\n\nChoice: ").lower()

                    if password_prompt == "1":
                        password = gp.getpass('Enter password: ')

                        if password == '':
                            print('Password cannot be empty.')
                            return

                        confirm_password = gp.getpass('Confirm password: ')
                        if password != confirm_password:
                            print('Passwords do not match.')
                            return
                            
                            new_password = password

                    elif password_prompt == "2":
                        new_password = gen_pass()

                        if new_password == None:
                            return
                        else:
                            return

                    old_password = fernet.decrypt(account.get("password").encode()).decode()

                    if new_password != old_password:
                        confirm = input(f"Changed password to: {new_password}? (Y/N): ").lower()

                        if confirm in ("y", "yes"):
                            encrypted_password = fernet.encrypt(new_password.encode()).decode()
                            account["password"] = encrypted_password
                            print("Successfully changed password!")
                            return data

                elif modify_prompt == "3":
                    new_notes = input("Enter new notes: ")

                    if new_notes != account.get("notes"):
                        if new_notes == "":
                            new_notes = "User did not enter notes."

                        account["notes"] = new_notes
                        print("Successfully changed notes!")
                        return data
            else:
                return
        
    print(f"\n{tags}\n")
    print("Account not found.")
    print(f"\n{tags}\n")
