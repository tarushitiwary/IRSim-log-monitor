from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
from log_parser import parse_logs

class LogHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith("access.log"):
            parse_logs(event.src_path)

def monitor_log(file_path):
    event_handler = LogHandler()
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
