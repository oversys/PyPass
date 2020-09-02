# PyPass
A simple Python Password Manager to allow you to save your passwords and interact with them. Features strong encryption with a 1-time key generation system.

# Instructions
* Run the "PyPass.py" file.
* Run the following command in the terminal of your OS: `pip install pyperclip`
* On first time use, a "database.json" file will be generated along with a "key.key" file. Make sure to store this key, without it, you will be unable to access the "database.json" file (it is encrypted).
* When you want to open the program, paste the "key.key" file in the "PyPass" directory.
* The operations and actions are listed in the program.
* Once done with the program, you can use the exit operation, use a keyboard interrupt(^C), or "X" out of the program. The "database.json" will be automatically encrypted.
* Cut the "key.key" file and paste it somewhere in your machine that no one knows about.
* This cut and paste back system is done as to prevent unauthorized access. In future updates, I may add an open file dialogue.

## Build 1 - August 13, 2020
* Basic features released

## Build 2 - August 15, 2020
* Increased security by doing the following:
  - Passwords are hidden when adding new accounts
  - Passwords are encrypted and only get decrypted when searching for an individual account or in the confirm to delete account prompt.
* Database files from Build 1 will not work on Build 2+.
 
 ## Build 3 - August 16, 2020
 * Re-structured the code (credits to hankhank10 - https://github.com/hankhank10/PyPass)
 * Program works differently now
 * Fixed a major security flaw
 * Removed the atexit library
 
 ## Build 4 - August 16, 2020
  * Added huge "PyPass" text on program start
  * Fixed a few missing "."s
  * Website names are no longer saved in their ".lower()" version
  * Fixed all notes being saved as "User did not enter notes."
  * Causing a Keyboard Interrupt in any of the information prompts of the "Add Account" feature will now send you back to the select operation menu
  * Causing a Keyboard Interrupt in the confirm to delete account prompt will now send you back to the select operation menu
  * Causing a Keyboard Interrupt in the select operation menu no longer throws an error, instead it will exit the program peacefully

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
  * Added the following libraries: "secret", "string", "pyperclip"
  * Users will now need to install the "pyperclip" library
  * Added copy to clipboard feature when looking up a specific account (this needs "pyperclip")
  * When adding new account, if the user accepted a generated password, the password will be copied to clipboard

## Build 7 - September 2, 2020
  * Added "Edit Account" feature that allows you to edit Username, Password, and notes.
  * Created "Assets" directory
  * Imported the ".move()" function from the "shutil" library
  * Cleaned up the code slightly by moving the "PYPASS" intro text to the Assets directory
  * Database file is now stored in the Assets directory
  * If the "database.json" file is still in the main directory, it will be moved automatically
