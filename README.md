# URL Shortener Application

This is a simple Windows application that monitors the clipboard for URLs and shortens them using the is.gd service. The application runs in the system tray and provides options to add or remove itself from startup.

## Features

- Automatically shortens URLs copied to the clipboard.
- Runs in the system tray with a custom icon.
- Options to add/remove the application from Windows startup.
- Lightweight and efficient.

## How to Use

1. **Download and Run**: Download the executable file from the releases section and run it.
2. **System Tray Icon**: Once running, the application will appear in the system tray with a custom icon.
3. **Clipboard Monitoring**: The application will continuously monitor the clipboard. When a URL is copied, it will automatically shorten it and replace the clipboard content.
4. **Startup Options**: Right-click the system tray icon to see options for adding or removing the application from startup, or to quit the application.

## How It Works

The application uses the is.gd service to shorten URLs and monitors the clipboard for any copied URLs. It then replaces the clipboard content with the shortened URL. The system tray icon provides a user-friendly way to manage the application's startup behavior.

## How It Was Made

### Tools and Libraries

- **Python**: The core programming language used for the application.
- **pyperclip**: Library for clipboard interaction.
- **requests**: Library for making HTTP requests to the is.gd API.
- **pystray**: Library for creating the system tray icon and menu.
- **Pillow**: Library for handling the icon image.
- **PyInstaller**: Tool for packaging the Python script into a single executable file.

### Development Steps

1. **Script Development**: Wrote the Python script to monitor the clipboard, shorten URLs, and manage the system tray icon.
2. **Icon Creation**: Created a custom icon for the system tray.
3. **Packaging**: Used PyInstaller to package the script into a single executable file.
4. **Testing**: Tested the executable on a Windows machine to ensure it worked as expected.

## Installation

To package the application yourself:

1. **Clone the Repository**: Clone this repository to your local machine.
2. **Install Dependencies**: Ensure you have Python installed along with the necessary libraries (`pyperclip`, `requests`, `pystray`, `Pillow`).
3. **Create Executable**: Use PyInstaller with the provided `.spec` file to create a single executable file.
