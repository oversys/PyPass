# PyPass
A simple Python Password Manager to allow you to securely save your usernames & passwords and interact with them. Features strong encryption with a 1-time key generation system.

# Instructions
  * Open the `PyPass.py` file.
  * (Optional) If you wish to have "copy to clipboard" features then run `pip install pyperclip` in your terminal.
  * On first time use, a `database.json` file will be generated along with a `key.key` file. DO NOT LOSE ANY OF THOSE FILES.
  * Make sure to hide the `key.key` file somewhere secure, you will be prompted to browse for the file and open it when you open the program.

## Build 1 - August 13, 2020
  * Basic features released

## Build 2 - August 15, 2020
  * Increased security by doing the following:
    - Passwords are hidden when adding new accounts
    - Passwords are encrypted and only get decrypted when searching for an individual account or in the confirm to delete account prompt
  * Database files from Build 1 will not work on Build 2+
 
 ## Build 3 - August 16, 2020
  * Program re-written (credits to hankhank10 - https://github.com/hankhank10/PyPass)
  * Fixed a major security flaw
  * Removed the `atexit` library
 
 ## Build 4 - August 16, 2020
  * Added "PyPass" title text on program start
  * Fixed a few missing "."s
  * Website names are no longer saved in lowercase
  * Fixed all notes being saved as "User did not enter notes."
  * Causing a Keyboard Interrupt in any of the information prompts of the "Add Account" feature will now send you back to the select operation menu
  * Causing a Keyboard Interrupt in the confirm to delete account prompt will now send you back to the select operation menu
  * Causing a Keyboard Interrupt in the select operation menu no longer throws an error, instead it will exit the program

## Build 5 - August 20, 2020
  * Added dates to new build version in the `README.MD` file
  * Added confirm password prompt when adding new account
  * Better exit handling implemented
  * "#"s are no longer hardcoded, instead a new variable called "tag" was added with the content of "# * 10"

## Build 6 - August 21, 2020
  * Code is more consistent and is cleaner
  * Added option to randomly generate passwords when adding account
  * Fixed a bug regarding multiple choice selection
  * Replaced "#"s with "—"s
  * Added the following libraries: `secret`, `string`, `pyperclip`
  * If installed on local machine, `pyperclip` will be used to increase program convenience
  * Added copy to clipboard feature when looking up a specific account (this needs `pyperclip`)
  * When adding new account, if the user accepted a generated password, the password will be copied to clipboard

## Build 7 - September 2, 2020
  * Added "Edit Account" feature that allows you to edit Username, Password, and notes
  * Created "Assets" directory
  * Imported 2 features from 2 libraries: `move()` from `shutil`, `urlopen()` from `urllib.request`
  * Cleaned up the code slightly by moving the "PYPASS" title text to the Assets directory
  * Database file is now stored in the Assets directory
  * If the `database.json` file is still in the main directory, it will be moved automatically
  * If the `Assets/text.txt` file is not found, it will be automatically retrieved from this repo. If the internet is disconnected then this process will fail.

## Build 8 - February 24, 2021
  * Imported `filedialog` from `tkinter`
  * Replaced the inconvenient cut-and-paste key system. Now, when you open the program and the `database.json` file exists, you will be prompted with a GUI to browse to and open     the `key.key` file.
  * Reformatted and slighty modified the `README.MD` file
  * Added option to "Reset Data" in the main menu (option X)
  * Minor modifications to the "Main Loop" code
  * Updated instructions
  * Fixed the "PYPASS" title text appearing as irrelevant characters by changing the encoding to "utf-8" when opening the `text.txt` file
  * Fixed the "PYPASS" title text failing to download when the `text.txt` file is missing
  * Major bug fixes within first-time setup
  * Improved program consistency
  * Switched between Search or Delete account options (C was deleted and D was search)
