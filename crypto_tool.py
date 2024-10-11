# crypto_tool.py
from cryptography.fernet import Fernet
import argparse
import os

def load_key(key_file):
    try:
        with open(key_file, 'rb') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Keyfile {key_file} not found.")
        exit(1)

def encrypt_file(key, file_name):
    try:
        with open(file_name, 'rb') as file:
            data = file.read()

        fernet = Fernet(key)
        encrypted_data = fernet.encrypt(data)

        encrypted_file_name = file_name + '.encrypted'
        with open(encrypted_file_name, 'wb') as encrypted_file:
            encrypted_file.write(encrypted_data)
        
        print(f"File {file_name} is encrypted as {encrypted_file_name}")

    except FileNotFoundError:
        print(f"File {file_name} not found.")

def decrypt_file(key, file_name):
    if not file_name.endswith('.encrypted'):
        print(f"File {file_name} is not encrypted (.encrypted förväntas).")
        return

    try:
        with open(file_name, 'rb') as file:
            encrypted_data = file.read()

        fernet = Fernet(key)
        decrypted_data = fernet.decrypt(encrypted_data)

        original_file_name = file_name.replace('.encrypted', '')
        with open(original_file_name, 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data)
        
        print(f"File {file_name} is decrypted and saved as {original_file_name}")

    except FileNotFoundError:
        print(f"File {file_name} not found.")
    except Exception as e:
        print(f"failed to decrypt {file_name}. error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="encrypt or decrypt file.")
    parser.add_argument("operation", choices=["encrypt", "decrypt"], help="Choose: 'encrypt' or 'decrypt'")
    parser.add_argument("key_file", help="Name for key to use for encrypt/decrypt.")
    parser.add_argument("file_name", help="Name of file to encrypt/decrypt.")
    
    args = parser.parse_args()
    
    key = load_key(args.key_file)

    if args.operation == "encrypt":
        encrypt_file(key, args.file_name)
    elif args.operation == "decrypt":
        decrypt_file(key, args.file_name)

#python crypto_tool.py encrypt <namn nyckel> <namn fil>
#python crypto_tool.py decrypt <namn nyckel> <namn fil>