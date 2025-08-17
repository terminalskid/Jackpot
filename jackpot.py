#!/usr/bin/env python3
import subprocess
import sys
import os
import time
import shutil

# List of required modules
required_modules = ["piexif", "exifread", "pillow"]

def install(module):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", module])
        print(f"Successfully installed {module}")
    except subprocess.CalledProcessError:
        print(f"Error installing {module}. Please install it manually.")

# Check and install missing modules
for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        print(f"Module {module} not found, installing...")
        install(module)

def get_python_command():
    return "python" if shutil.which("python") else "py"

# -------- Settings -------- #
AUTHOR = "@terminalskid"
TITLE = "Jackpot"
TOOL_COUNT = 11

# Get home directory dynamically
HOME_DIR = os.path.expanduser("~")
BASE_PATH = os.path.join(HOME_DIR, "Downloads", "Jackpot-main", "Program")

# Define tool paths and names
TOOL_PATHS = {
    "1": (os.path.join(BASE_PATH, "image-data.py"), "Image Data"),
    "2": (os.path.join(BASE_PATH, "dark-web.py"), "Dark Web"),
    "3": (os.path.join(BASE_PATH, "email-lookup.py"), "Email Lookup"),
    "4": (os.path.join(BASE_PATH, "ip-lookup.py"), "IP Lookup"),
    "5": (os.path.join(BASE_PATH, "phisher.py"), "Phishing Script"),
    "6": (os.path.join(BASE_PATH, "phone-lookup.py"), "Phone Number Lookup"),
    "7": (os.path.join(BASE_PATH, "username-tracker.py"), "Username Tracker"),
    "8": (os.path.join(BASE_PATH, "ip-scanner.py"), "IP Scanner"),
    "9": (os.path.join(BASE_PATH, "Ip-Port-Scanner.py"), "IP Port Scanner"),
    "10": (os.path.join(BASE_PATH, "ip-generator.py"), "IP Generator"),
    "11": (os.path.join(BASE_PATH, "Ip-Pinger.py"), "IP Pinger"),
}

# Global variable for page navigation
current_page = 1
tools_per_page = 15

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def ascii_banner():
    return r"""
      ██╗ █████╗  ██████╗██╗  ██╗██████╗  ██████╗ ████████╗
      ██║██╔══██╗██╔════╝██║ ██╔╝██╔══██╗██╔═══██╗╚══██╔══╝
      ██║███████║██║     █████╔╝ ██████╔╝██║   ██║   ██║   
 ██   ██║██╔══██║██║     ██╔═██╗ ██╔═══╝ ██║   ██║   ██║   
 ╚█████╔╝██║  ██║╚██████╗██║  ██╗██║     ╚██████╔╝   ██║   
  ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝      ╚═════╝    ╚═╝   

                Terminal Multitool by @terminalskid
    """

def show_menu():
    global current_page
    clear()
    print(ascii_banner())
    print(f"Current Page: {current_page} / {max_pages()}\n")

    start = (current_page - 1) * tools_per_page
    end = min(start + tools_per_page, TOOL_COUNT)

    for i in range(start, end):
        code = str(i + 1)
        name = TOOL_PATHS[code][1]
        print(f"  [{code}] {name}")

    print("\n[H] Help   [N] Next Page   [P] Prev Page   [Q] Quit")

def max_pages():
    return (TOOL_COUNT + tools_per_page - 1) // tools_per_page

def launch_tool(code):
    if code in TOOL_PATHS:
        print(f"\n>> Launching {TOOL_PATHS[code][1]} — handled by ({AUTHOR})\n")
        time.sleep(0.3)
        tool_path = TOOL_PATHS[code][0]
        
        if os.path.exists(tool_path):
            os.system(f'py "{tool_path}"')  # Run the script if path is valid
        else:
            print(f"Error: {tool_path} does not exist. Please check the tool path.")
    else:
        print(f"\n>> No tool configured for code '{code}'.")

def show_help():
    print("\nHelp Section:")
    print("For more tools and information, visit: https://guns.lol/skidboi")
    input("\nPress Enter to return to the menu...")

def main():
    global current_page
    while True:
        show_menu()
        user_input = input("\n> Enter code or command: ").strip().lower()

        if user_input == 'q':
            print("\nExiting Jackpot. See you soon!")
            break
        elif user_input == 'h':
            show_help()
        elif user_input == 'n':
            if current_page < max_pages():
                current_page += 1
            else:
                print("Already at the last page.")
                time.sleep(1)
        elif user_input == 'p':
            if current_page > 1:
                current_page -= 1
            else:
                print("Already at the first page.")
                time.sleep(1)
        elif user_input in TOOL_PATHS:
            launch_tool(user_input)
            input("\nPress ENTER to return to the menu...")
        else:
            print("Invalid input. Use the tool number (e.g., 1, 2...) or 'exit' or 'help'.")
            time.sleep(1)

if __name__ == "__main__":
    main()
