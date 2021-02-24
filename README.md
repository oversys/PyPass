# PyPass
A simple Python Password Manager to allow you to save your passwords and interact with them. Features strong encryption with a 1-time key generation system.

# Instructions
* Open the `PyPass.py` file.
* (Optional) If you wish to have "copy to clipboard" features then run `pip install pyperclip` in your terminal.
* On first time use, a `database.json` file will be generated along with a `key.key` file. Make sure to store this key, without it, you will be unable to access the `database.json` file (it is encrypted).
* When you want to open the program, paste the `key.key` file in the "PyPass" directory.
* Once done with the program, cut the `key.key` file and hide it somewhere secure.
* This cut and paste back system is done as to prevent unauthorized access.

### You may either download all the files in this repo or download the "PyPass.py" file and the necessary files will be created automatically (database.json, key.key for first time use. text.txt if not found).

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
  * Added dates to new build version in the "README.MD" file
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
