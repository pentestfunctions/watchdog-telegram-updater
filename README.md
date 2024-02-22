# Watchdog Telegram Updater :dog2: :bell:

The **Watchdog Telegram Updater** is a Python tool that utilizes the `watchdog` library to monitor file changes and updates users through Telegram messages. Whenever a specified file is modified, it sends a detailed message to a Telegram chat containing the changes made. This tool is perfect for real-time monitoring of log files, configuration files, or any file where changes need to be tracked and communicated instantly.

## Features :sparkles:
- Real-time monitoring of file modifications.
- Sends detailed change logs to a Telegram chat.
- Easy to set up and use with minimal configuration.
- Filter words to ignore certain modifications (Future improvement).

## Getting Started :rocket:
Before you begin, ensure you have Python installed on your system. This tool also requires a Telegram bot token and a chat ID where the messages will be sent.

### Prerequisites
- Python 3.x
- `requests` library
- `watchdog` library

### Installation
1. Clone the repository:
```bash
git clone https://github.com/pentestfunctions/watchdog-telegram-updater.git
```

2. Install the required libraries:
```bash
pip install requests watchdog
```

3. Enter your Telegram bot token and chat ID in the script.

## Usage :computer:
To start monitoring a file, run the script with Python:
```bash
python telegram-watchdog.py
```
Make sure to modify the `file_to_watch` variable in the script to point to the file you want to monitor.

## Ideas for Future Improvement :bulb:

- **Filter Words:** Implement functionality to ignore changes containing specific keywords or patterns.
- **Multiple File Support:** Extend the tool to monitor multiple files simultaneously.
- **Customizable Alerts:** Allow users to customize the alert message format.
- **Web Interface:** Develop a web interface for easier management and monitoring of file changes.

## Contributing :handshake:

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

License :page_facing_up:
Distributed under the WTFPL License. See LICENSE for more information.

Acknowledgments :clap:
- The `watchdog` library for providing the file monitoring functionality.
- The `requests` library for simplifying HTTP requests.
