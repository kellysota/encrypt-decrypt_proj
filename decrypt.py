# Modules
from cryptography.fernet import Fernet
import os

class Decryptor:
    def loadkey(self, key_name):
        key = open(key_name,"rb").read()
        return key
    
    def decrypt(self, path, key):
        for path, sub_dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(path, file)

                if file_path.endswith(".aes"):
                    self.decrypt_all_files(file_path, key)


    def decrypt_all_files(self, file, key):
        f = Fernet(key)
        decrypted = f.decrypt(open(file, "rb").read())

        with open(file.replace(".aes", ""), "wb") as decrypted_file:
            decrypted_file.write(decrypted)

        # Supprimer les docs originaux
        os.remove(file)



if __name__ == "__main__":
    decryptor = Decryptor()

    key = decryptor.loadkey("key.key")

    doc = input("Enter the folder name you wish to decrypt: ")

    decryptor.decrypt(doc,key)