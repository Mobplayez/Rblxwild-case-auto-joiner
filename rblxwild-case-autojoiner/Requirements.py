import os
import base64
import shutil
import marshal
import traceback
import subprocess

if "Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Manage App Execution Aliases." in subprocess.check_output("python --version").decode():
    os.system("powershell Remove-Item $env:LOCALAPPDATA\Microsoft\WindowsApps\python.exe") # Remove the bugged app alias that Microsoft added (Because Microsoft doesn't do anything right)
    os.system("cls")

if "is not recognized" in subprocess.check_output("python --version").decode():
    print("Python is not added to PATH! Reinstall Python and make sure to tick the Add Python to PATH box!")
    while True: pass

os.system("python -m pip install pyinstaller pypiwin32 pycryptodome requests")
os.system("cls")

if "is not recognized" in subprocess.check_output("pyinstaller --version").decode():
    print("Python is not added to PATH! Reinstall Python and make sure to tick the Add Python to PATH box!")
    while True: pass
