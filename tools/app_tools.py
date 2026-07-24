import subprocess

APP_PATHS = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "cmd": "cmd.exe"
}

def open_app(app_name: str):
    app = app_name.lower()

    if app not in APP_PATHS:
        return f"Unknown application: {app}"

    subprocess.Popen(APP_PATHS[app])

    return f"{app} opened successfully."