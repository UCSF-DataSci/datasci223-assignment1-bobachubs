#!/usr/bin/env python3
"""
Email Hasher Script

This script takes an email address as a command line argument,
hashes it using the SHA-256 algorithm, and writes the hash to a file.

Usage:
    python email_hasher.py <email_address>

Example:
    python email_hasher.py example@email.com
"""

import sys
import hashlib
import re

def hash_email(email):
    """
    Hash an email address using SHA-256 and return the hexadecimal digest.
    
    Args:
        email (str): The email address to hash
        
    Returns:
        str: The SHA-256 hash of the email in hexadecimal format
    """
    # TODO: Implement this function
    # 1. Convert the email string to bytes
    # 2. Create a SHA-256 hash of the email
    # 3. Return the hash in hexadecimal format
    str_byte = str.encode(email)
    m = hashlib.sha256(str_byte)
    hex = m.hexdigest()
    return hex

def write_hash_to_file(hash_value, filename="hash.email"):
    """
    Write a hash value to a file.
    
    Args:
        hash_value (str): The hash value to write
        filename (str): The name of the file to write to (default: "hash.email")
    """
    # TODO: Implement this function
    # 1. Open the file in write mode
    # 2. Write the hash value to the file
    # 3. Close the file
    print(hash_value)
    with open(filename, 'w') as f:
        f.write(hash_value)
    f.close()
    return hash_value

def main():
    """
    Main function to process command line arguments and execute the script.
    """
    # TODO: Implement this function
    # 1. Check if an email address was provided as a command line argument
    # 2. If not, print an error message and exit with a non-zero status
    # 3. If yes, hash the email address
    # 4. Write the hash to a file named "hash.email"

    if len(sys.argv) != 2:
        raise Exception("Please input a valid email")
    email = sys.argv[1]
    email_hash = hash_email(email)
    write_hash_to_file(email_hash, 'hash.email')
    return

if __name__ == "__main__":
    main()

