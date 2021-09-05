# PyPass
A simple Python Password Manager to allow you to securely save your usernames & passwords and interact with them. Features encryption with a 1-time key generation system.

# Instructions
  * (Required) Run `pip install cryptography` (Windows) or `pip3 install cryptography` (Linux) in your terminal
  * (Optional) If you wish to have "copy to clipboard" features then run `pip install pyperclip` (Windows) or `pip3 install pyperclip` (Linux) in your terminal
  * Open the `PyPass.py` file. Windows: Double Click. Linux: Open the terminal in the PyPass folder and run `python3 PyPass.py`
  * On first time use, a `database.json` file will be generated along with a `key.key` file. DO NOT LOSE ANY OF THOSE FILES.
  * Make sure to hide the `key.key` file somewhere secure, you will be prompted to browse for the file and open it when you open the program.

## Build 1 - August 13, 2020
  * Basic features released

## Build 2 - August 15, 2020
  * Added new security features:
    - Passwords are hidden when adding new accounts
    - Passwords are encrypted and only get decrypted when searching for an individual account or deleting an account
  * Database files from Build 1 will not work on Build 2+
 
 ## Build 3 - August 16, 2020
  * Program re-written (credits to hankhank10 - https://github.com/hankhank10/PyPass)
  * Fixed a major security flaw
  * Removed the `atexit` library
  * Added "PyPass" title text on program start
  * Fixed a few typos
  * Website names are no longer saved in lowercase
  * Fixed all notes being saved as "User did not enter notes."
  * Causing a Keyboard Interrupt in any of the information prompts of the "Add Account" feature will now send you back to the select operation menu
  * Causing a Keyboard Interrupt in the confirm to delete account prompt will now send you back to the select operation menu
  * Causing a Keyboard Interrupt in the select operation menu no longer throws an error, instead it will exit the program

## Build 4 - August 20, 2020
  * Added dates to new builds in the `README.MD` file
  * Added confirm password prompt when adding new account
  * Better exit handling implemented
  * "#"s are no longer hardcoded

## Build 5 - August 21, 2020
  * Cleaned up the code to make it more consistent
  * Added an option to generate passwords when adding an account
  * Fixed a bug regarding multiple choice selection
  * Replaced "#"s with "—"s
  * Added the following libraries: `secret`, `string`, `pyperclip`
  * Decrypted passwords will automatically be copied to clipboard when searching for a specific account (This feature requires `pyperclip`)
  * When adding a new account, if the user accepted a generated password, the password will be copied to clipboard (This feature requires `pyperclip`)

## Build 6 - September 2, 2020
  * Added "Edit Account" feature that allows you to edit username, password, and notes
  * Created "Assets" directory
  * Imported 2 features from 2 libraries: `move()` from `shutil`, `urlopen()` from `urllib.request`
  * Cleaned up the code slightly
  * Database file is now stored in the Assets directory
  * If the `database.json` file is still in the main directory, it will be moved automatically
  * If the `Assets/text.txt` file is not found, it will be automatically retrieved from this repo. If the internet is disconnected then this process will fail.

## Build 7 - February 24, 2021
  * Imported `filedialog` from `tkinter`
  * Replaced the inconvenient cut-and-paste key system. Now, when you open the program and the `database.json` file exists, you will be prompted with a GUI to browse to and open the `key.key` file.
  * Reformatted and slighty modified the `README.MD` file
  * Added option to "Reset Data" in the main menu (option X)
  * Minor modifications to the "Main Loop" code
  * Updated instructions
  * Fixed the "PYPASS" title text appearing as irrelevant characters by changing the encoding to "utf-8" when opening the `text.txt` file
  * Fixed the "PYPASS" title text failing to download when the `text.txt` file is missing
  * Major bug fixes within first-time setup code
  * Improved program consistency
  * Switched between Search or Delete account options (C was deleted and D was search)
