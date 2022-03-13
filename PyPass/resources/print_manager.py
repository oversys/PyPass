import os

def print_actions():
    tags = '—' * 32

    print(f"""\n{tags}\nActions List:
    (1) View Accounts
    (2) Add Account
    (3) Search For Account
    (4) Modify Account
    (5) Delete Account
    (6) Generate Random Password
    (7) Check For Updates
    (Q) Quit
    (M) Change Master Password
    (X) RESET DATA\n{tags}\n""")

def print_pwd_opts():
    tags = '—' * 25

    print(f"""\n{tags}\nOptions List:
    (1) Enter Password
    (2) Generate Password
    (C) Cancel\n{tags}\n""")

def print_modify_opts():
    tags = '—' * 23

    print(f"""\n{tags}\nOptions List:
    (1) Modify Username
    (2) Modify Password
    (3) Modify Notes
    (C) Cancel\n{tags}\n""")

def clear():
    if os.name in ("nt", "dos"):
        print("\n" * 1000) 
        os.system("cls")
    else:
        print("\033c", end="")
