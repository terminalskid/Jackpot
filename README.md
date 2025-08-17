
---

# Jackpot Tool v1.0

**Jackpot Tool** is an open-source, all-in-one investigative tool for OSINT (Open Source Intelligence), security testing, and research. It includes features like image EXIF extraction, IP, email, and phone lookups, dark web exploration, username tracking, and phishing simulations.

This tool was **developed and used by the owner on Kali Linux**, and the setup guide below will walk you through installing and using it.

---

## Features

* **Image EXIF Data**: Extract metadata from images to trace back origins and modifications.
* **IP Lookup**: Search and retrieve information about an IP address.
* **Email Lookup**: Find details about an email address, including owner information.
* **Phone Lookup**: Trace phone numbers to their geographic location.
* **Dark Web Links**: Access curated links to explore the dark web for research purposes.
* **Username Tracker**: Track usernames across platforms and websites.
* **Phishing Simulator**: Test the security of email systems by running phishing simulations.

---

## Installation Guide

### **1. Prerequisites**

Before setting up **Jackpot Tool**, make sure you have the following installed:

* **Python 3.8+** (Recommended: Python 3.10+)
* **pip** (Python package installer)
* **Git** (for cloning the repository)

If you're using **Kali Linux**, most of these dependencies are already installed by default.

---

### **2. Setting Up on Kali Linux**

#### **Step 1: Clone the Repository**

Start by cloning the repository to your local machine:

```bash
git clone https://github.com/yourusername/jackpot-tool.git
cd jackpot-tool
```

#### **Step 2: Create a Virtual Environment (Optional but Recommended)**

It's best practice to create a virtual environment to avoid conflicts with other Python packages:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### **Step 3: Install Dependencies**

Install the required libraries using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

This will install all the necessary dependencies for **Jackpot Tool** to function correctly.

---

### **3. Running Jackpot Tool**

Once the dependencies are installed, you can start using **Jackpot Tool**.

1. **Start the tool**:

   ```bash
   python jackpot.py
   ```

2. Follow the on-screen instructions to use features like IP Lookup, Email Lookup, Phishing, and more.

---

## Supported Platforms

* **Kali Linux** (Primary OS for development and usage)
* **Debian-based Linux distributions** (Ubuntu, etc.)
* **Windows** (via WSL, or use native Python for Windows)
* **macOS** (with minor tweaks for dependencies)

---

## Requirements

* **Python 3.8+** (3.10+ recommended)
* **pip** (Python added to path)
* **Dependencies listed in `requirements.txt`** (installable via `pip install -r requirements.txt`)

---

## Features Overview

* **Image EXIF Lookup**: Analyze image metadata for detailed information like GPS coordinates, creation time, and modification history.
* **IP Lookup**: Perform a search on any IP address to see where it's located, whether it's private/public, and more.
* **Email Lookup**: Discover the origin of any email address and find out if it's associated with a known provider or a risky domain.
* **Phone Lookup**: Trace phone numbers to their respective countries and regions.
* **Dark Web Exploration**: Gain access to dark web links for research or investigation purposes.
* **Username Tracker**: Find where a username is used online across various social media platforms.
* **Phishing Simulation**: Simulate phishing attacks to test email systems and increase awareness of potential security risks.

---

## Contributing

Since **Jackpot Tool** is open-source, we encourage contributions! Feel free to fork the repository, make changes, and submit a pull request.

If you have ideas for new features, improvements, or find bugs, don’t hesitate to open an issue or pull request.

---

## License

**Jackpot Tool** is open-source and licensed under the MIT License. See the LICENSE file for more details.

---

## Troubleshooting

1. **Issue: Missing dependencies**
   Ensure all dependencies are installed using `pip install -r requirements.txt`. If you encounter any missing packages, try installing them manually.

2. **Issue: Permissions errors**
   If you face permission issues on Kali or other Linux-based systems, try running the installation commands with `sudo`, or ensure that you have the necessary privileges.

---

## Setup Guide on Other Platforms

While **Jackpot Tool** is developed and used on Kali Linux, it’s also possible to run on other platforms such as **Windows** or **macOS**.

Here are a few steps for setup on **Windows** and **macOS**:

### **For Windows Users (via WSL)**

1. Install **WSL (Windows Subsystem for Linux)**. Follow the [official guide](https://docs.microsoft.com/en-us/windows/wsl/install) to install a Linux distribution on your Windows system.
2. Follow the same **Linux setup instructions** after setting up WSL.
3. Run the tool by navigating to the folder and executing `python jackpot.py`.

### **For macOS Users**

1. Install **Homebrew** (if not already installed):

   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
2. Install **Python** and **pip** if not already installed:

   ```bash
   brew install python3
   ```
3. Follow the **Linux setup instructions** for macOS. If you face issues with dependencies, you can manually install them via **brew**.

---

## Contact & Support

For help or support, you can reach out by opening an issue or reaching out via the following channels:

* GitHub Issues: [https://github.com/terminalskid/Jackpot/issues](https://github.com/terminalskid/Jackpot/issues)
* Email: [support@jackpotdev.xyz](mailto:support@jackpotdev.xyz)

---
