# USER MANUAL

## Installation

To run the program we will need to have Python 3.6 installed.
To install Python 3.6 in a machine with Windows 7, 8, 8.1 or 10 we will need an user account with admin privileges or the local admistrator account.

In systems with 64 bit arquitecture you can install either the 32 bit or 64 bit version. In general, you will want to install the 64 bit version for better performance.

### Installation steps:

1. Go to https://www.python.org/downloads/windows/
2. Search for your desired version of Python.
3. Select a link to download either the Windows x86-64 executable installer or Windows x86 executable installer. The download is approximately 25MB.
4. Run the Python Installer once downloaded.
5. Make sure you select the Install launcher for all users and Add Python 3.7 to PATH checkboxes. The latter places the interpreter in the execution path. For older versions of Python that do not support the Add Python to Path checkbox.
6. Select Install Now – the recommended installation options.
7. The next dialog will prompt you to select whether to Disable path length limit. Choosing this option will allow Python to bypass the 260-character MAX_PATH limit. Effectively, it will enable Python to use long path names.
8. Navigate to the directory in which Python was installed on the system. In our case, it is C:\Users\Username\AppData\Local\Programs\Python\Python37 since we have installed the latest version.
9. Double-click python.exe.
10. Open the Start menu and type "cmd."
11. Select the Command Prompt application.
12. Enter pip -V in the console. You should see the pip install location.

## Usage

Open a command-line and type in the word python followed by the path to the script.
