# PyPass
A password manager written in Python. Data is encrypted using AES-128. Master password + salt are hashed using SHA-256 and the key is derived using PBKDF2. (Python3 and Pip3 are required)

#### You may encounter bugs while using this program. Feel free to open issues and/or submit pull requests.
#### I plan on adding a TUI (terminal user interface) to this program in the future.

# Instructions
_Assuming you have downloaded and unzipped the folder or cloned the repository._

 ### (Required) Install cryptography library:
 _Windows:_ Run this command in the command prompt: 
 ```
 pip install cryptography
 ```
 _Linux:_ Run this command in the terminal: 
 ```
 pip3 install cryptography
 ```
 ### (Optional) Install pyperclip library for "copy to clipboard features":
 _Windows:_ Run this command in the command prompt: 
 ```
 pip install pyperclip
 ```
 _Linux:_ Run this command in the terminal: 
 ```
 pip3 install pyperclip
 ```
 On some Linux systems, you may need to install a package called `xclip`. You will be notified when the program attempts to copy a string to clipboard if that is the case.
 
 ### Open the `PyPass.py` file:
 _Windows:_ Double click the file
  
 _Linux:_ Run this command in the terminal (In the PyPass directory): 
 ```
 python3 PyPass.py
 ```
 #### On first time use, a `database.json` file will be generated along with a `pw.json` file. _DO NOT MODIFY/DELETE EITHER OF THOSE FILES._

Check the [RELEASES.md](https://github.com/BetaLost/PyPass/blob/master/RELEASES.md) file for the update history and changelog.
