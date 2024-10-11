# generate_key.py
from cryptography.fernet import Fernet
import argparse

def generate_key(output_file):
    """
    Generate a key
    """
    key = Fernet.generate_key()
    with open(output_file, 'wb') as key_file:
        key_file.write(key)
    print(f"Key generated and saved to {output_file}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a symmetrical key and save it to a file.")
    parser.add_argument("output_file", help="name of file where the key is stored")
    args = parser.parse_args()
    generate_key(args.output_file)

#för att köra i terminal ==> python generate_key.py namnpåfilen