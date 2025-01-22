# libraries
from cryptography.fernet import Fernet
import os 


class Encryptor:
    def loadkey(self, key_name):
        key = open(key_name,"rb").read()
        return key
    def encrypt(self, path, key):
        for path, files in os.walk(path):
            for file in files:
                file_path = os.path.join(path, file)
                self.encrypt_all_files(file_path, key)


    def encrypt_all_files(self, file, key):
        f = Fernet(key)
        encrypted = f.encrypt(open(file, "rb").read())

        with open(file + ".aes", "wb") as encrypted_file:
            encrypted_file.write(encrypted)

        # Supprimer les docs originaux
        os.remove(file)



if __name__ == "__main__":
    encryptor = Encryptor()

    key = encryptor.loadkey("key.key")

    doc = input("Enter the folder name you wish to encrypt: ")

    encryptor.encrypt(doc,key)