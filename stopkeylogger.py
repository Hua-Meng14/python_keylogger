import psutil

# Find the keylogger process
for proc in psutil.process_iter():
    try:
        if 'python' in proc.name() and 'key_logger_bg.py' in ' '.join(proc.cmdline()):
            p = psutil.Process(proc.pid)
            # Kill the keylogger process
            p.terminate()
            print('Keylogger terminated.')
            break
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
