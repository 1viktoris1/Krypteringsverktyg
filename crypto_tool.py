#Encryprytd or decrypts file using an given key
import argparse
from cryptography.fernet import Fernet

def load_key(key_file):
    """Loads a key from file"""
    try:
        with open(key_file, 'rb') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Keyfile {key_file} not found.")
        exit(1)

def encrypt_file(key, file_name):
    """Encrypts a file using the provided key"""
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
    except PermissionError:
        print(f"No rights to file {file_name}.")

def decrypt_file(key, file_name):
    """Decrypts an encrypted file using the provided key"""
    if not file_name.endswith('.encrypted'):
        print(f"File {file_name} is not encrypted (.encrypted is expected).")
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
    except PermissionError:
        print(f"No rights to open {file_name}.")

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

# Example usage:
#python crypto_tool.py encrypt <namn nyckel> <namn fil>
#python crypto_tool.py decrypt <namn nyckel> <namn fil>
