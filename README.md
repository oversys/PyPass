# ![PyPass](logo.png)
A password manager written in Python. Data is encrypted using AES-256-GCM and the key is derived using PBKDF2-HMAC-SHA512.

*Check the [RELEASES.md](https://github.com/oversys/PyPass/blob/master/RELEASES.md) file for the update history and changelog.*

*Keep a backup of the `database.json` & `info.json` files.*

*Commit history cleared at 202 commits (25 June 2024).*

#### You may encounter bugs while using this program. Feel free to open issues and/or submit pull requests.

##### Python 3.10+ is required.

## Features
#### Minimal Dependencies
Just one required dependency which is used for encryption and hashing and one optional dependency for copy-to-clipboard features.

#### "Bulletproof" Military-Grade Encryption
Virtually impenetrable through means of brute-force attacks.

#### Easy to update
You can update the program using a built-in feature rather than cloning this repository every time.

#### Easy to use
Clear instructions and simple to use.

# Instructions
*Assuming you have cloned the repository or downloaded and unzipped the folder. Python3 and Pip3 are required.*

### (Required) Install cryptography library:
*Windows & Linux:* Run this command in the terminal: 
```
pip3 install cryptography
```
### (Optional) Install pyperclip library for "copy to clipboard features":
*Windows & Linux:* Run this command in the terminal: 
```
pip3 install pyperclip
```
On some Linux systems, you may need to install a package called `xclip`. You will be notified when the program attempts to copy a string to clipboard if that is the case. Consult your distribution's wiki for instructions on installing packages if you do not know how to do that.

### Open the `PyPass.py` file:
*Windows & Linux:* Run this command in the terminal (in the directory that contains the main `PyPass.py` file): 
```
python3 PyPass.py
```
