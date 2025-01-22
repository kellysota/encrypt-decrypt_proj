from cryptography.fernet import Fernet

def write_key(key_name): 
    # Clé
    key = Fernet.generate_key()

    with open(key_name, 'wb') as key_file:
        key_file.write(key)


if __name__ =="__main__":
    write_key("key.key")