# Hashing Tool

### Background

This tool can be used to generate a target file's hash value using the SHA-256 algorithm.

### Using the program

The code can be run directly from the terminal or it can be packaged into a .exe and run independently (which is how it is currently being used).

To run the program from the terminal, navigate to the directory you have saved the files and run: `python hash_app.py`

To package the code into a .exe using pyinstaller (https://www.pyinstaller.org/) first pip install pyinstaller. Then run: `pyinstaller -w -F -i hash_app_icon.ico hash_app.spec hash_app.py`

NB: the code has only been used and tested on the Windows 10 operating system.

### Code used

This program is written in Python 3.6.5, with the user interface developed in tkinter.