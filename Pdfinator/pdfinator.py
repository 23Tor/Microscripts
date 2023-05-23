import time
import os
from PIL import Image
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return

        file_extensions = (".jpg", ".png", ".jpeg", ".tiff", ".bmp")
        if event.src_path.endswith(file_extensions):
            time.sleep(0.1)
            pdf_path = os.path.splitext(event.src_path)[0] + ".pdf"

            while True:
                try:
                    with Image.open(event.src_path) as img:
                        if event.src_path.endswith((".png", ".tiff")):
                            img = img.convert("RGB")
                        img.save(pdf_path, "PDF", resolution=100.0)
                    break
                except PermissionError:
                    time.sleep(0.1)

            time.sleep(0.1)
            while True:
                try:
                    os.remove(event.src_path)
                    break
                except PermissionError:
                    time.sleep(0.1)


if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()

    paths = [
        "One/Of/Many/Folder/Paths",
        "Two/Of/Many/Folder/Paths"
    ]

    for path in paths:
        observer.schedule(event_handler, path=path, recursive=False)

    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()