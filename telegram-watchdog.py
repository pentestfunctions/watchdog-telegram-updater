import time
import difflib
import requests
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

def send_telegram_message(token, chat_id, message):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    print(f"Current data being sent: {message}")
    response = requests.post(url, data=data)
    return response.json()

class FileUpdateHandler(PatternMatchingEventHandler):
    def __init__(self, patterns, file_path, token, chat_id):
        super().__init__(patterns=patterns)
        self.file_path = file_path
        self.token = token
        self.chat_id = chat_id
        self.last_content = self.read_file_content()

    def on_modified(self, event):
        new_content = self.read_file_content()
        diff = difflib.unified_diff(self.last_content, new_content, lineterm='', fromfile='before', tofile='after')
        
        filtered_diff = [line for line in diff if not line.startswith('---') and not line.startswith('+++')]
        diff_text = '\n'.join(filtered_diff).replace('- ', '').replace('+ ', 'Change: ')

        if diff_text:
            send_telegram_message(self.token, self.chat_id, f"File {event.src_path} has been updated.\nChanges:\n{diff_text}")
        self.last_content = new_content

    def read_file_content(self):
        with open(self.file_path, 'r') as file:
            return file.readlines()

if __name__ == "__main__":
    path = "./"
    file_to_watch = "outputfile.txt"
    full_file_path = f"{file_to_watch}"
    # Add chat_id and bot token here. Token is digits:string format
    telegram_bot_token = ""
    telegram_chat_id = ""

    event_handler = FileUpdateHandler([f"*{file_to_watch}"], full_file_path, telegram_bot_token, telegram_chat_id)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
