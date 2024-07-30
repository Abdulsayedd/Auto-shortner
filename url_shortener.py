import pyperclip
import requests
import threading
import pystray
from PIL import Image
import os
import shutil
from pathlib import Path
from pystray import MenuItem as item
import time
import sys

# Function to shorten URL using is.gd
def shorten_url(url):
    api_url = "https://is.gd/create.php"
    params = {
        'format': 'simple',
        'url': url
    }
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        return response.text
    else:
        return url

# Function to check and shorten URL in clipboard
def check_clipboard():
    recent_value = ""
    while True:
        tmp_value = pyperclip.paste()
        if tmp_value != recent_value and tmp_value.startswith("http"):
            shortened_url = shorten_url(tmp_value)
            pyperclip.copy(shortened_url)
            recent_value = shortened_url
        time.sleep(1)

# Function to add the executable to startup
def add_to_startup(icon, item):
    startup_dir = Path(os.getenv('APPDATA')) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"
    exe_path = Path(sys.argv[0]).resolve()
    startup_path = startup_dir / exe_path.name
    if not startup_path.exists():
        shutil.copy(exe_path, startup_path)
    update_menu(icon)

# Function to remove the executable from startup
def remove_from_startup(icon, item):
    startup_dir = Path(os.getenv('APPDATA')) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"
    exe_path = Path(sys.argv[0]).resolve()
    startup_path = startup_dir / exe_path.name
    if startup_path.exists():
        os.remove(startup_path)
    update_menu(icon)

# Function to check if the executable is in the startup folder
def is_in_startup():
    startup_dir = Path(os.getenv('APPDATA')) / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"
    exe_path = Path(sys.argv[0]).resolve()
    startup_path = startup_dir / exe_path.name
    return startup_path.exists()

# Function to update the system tray menu
def update_menu(icon):
    if is_in_startup():
        icon.menu = pystray.Menu(
            item("Remove from Startup", remove_from_startup),
            item("Quit", quit_application)
        )
    else:
        icon.menu = pystray.Menu(
            item("Add to Startup", add_to_startup),
            item("Quit", quit_application)
        )
    icon.update_menu()

# Function to quit the application
def quit_application(icon, item):
    icon.stop()
    # To clean up the clipboard watcher thread
    global checker_thread
    if checker_thread.is_alive():
        checker_thread.join()

if __name__ == "__main__":
    # Load the icon
    icon_image = Image.open("E:\\testcopy\\copy.ico")
    icon = pystray.Icon("url_shortener", icon_image, "URL Shortener")
    
    # Update the menu based on startup status
    update_menu(icon)
    
    # Run the clipboard checker in a separate thread to keep the tray icon responsive
    checker_thread = threading.Thread(target=check_clipboard)
    checker_thread.daemon = True
    checker_thread.start()

    icon.run()
