# PyPass
A simple Python Password Manager to allow you to save your passwords and interact with them. Features strong encryption with a 1-time key generation system.

# Instructions
* Run the "PyPass.py" file.
* On first time use, a "database.json" file will be generated along with a "key.key" file. Make sure to store this key, without it, you will be unable to access the "database.json" file (it is encrypted).
* When you want to open the program, paste the "key.key" file in the "PyPass" directory.
* The operations and actions are listed in the program.
* Once done with the program, you can use the exit operation, use a keyboard interrupt(^C), or "X" out of the program. The "database.json" will be automatically encrypted.
* Cut the "key.key" file and paste it somewhere in your machine that no one knows about.
* This cut and paste back system is done as to prevent unauthorized access. In future updates, I may add an open file dialogue.

## Build 1
* Basic features released

## Build 2
* Increased security by doing the following:
  - Passwords are hidden when adding new accounts
  - Passwords are encrypted and only get decrypted when searching for an individual account or in the confirm to delete account prompt.
* Database files from Build 1 will not work on Build 2+.
 
 ## Build 3
 * Re-structured the code (credits to hankhank10 - https://github.com/hankhank10/PyPass)
 * Program works differently now
 * Fixed a major security flaw
 * Removed the atexit library
 
 ## Build 4
  * Added huge "PyPass" text on program start
  * Website names are no longer saved in their ".lower()" version
  * Fixed all notes being saved as "User did not enter notes."
  * Causing a Keyboard Interrupt in any of the information prompts of the "Add Account" feature will now send you back to the select operation menu
  * Causing a Keyboard Interrupt in the confirm to delete account prompt will now send you back to the select operation menu
  * Causing a Keyboard Interrupt in the select operation menu no longer throws an error, instead it will exit the program peacefully
