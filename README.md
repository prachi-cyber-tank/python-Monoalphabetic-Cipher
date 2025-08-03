Monoalphabetic Cipher

A simple, command-line tool for encrypting and decrypting text using the Monoalphabetic Substitution Cipher. This project is intended for educational purposes to demonstrate a basic cryptographic concept.

What is a Monoalphabetic Cipher?

A monoalphabetic substitution cipher is a classic encryption technique where each letter in the plaintext (the original message) is consistently replaced with a different letter from the alphabet. The "key" for this cipher is the mapping of each letter to its substitute. For this to work, the key must be a permutation of the alphabet, meaning every letter of the alphabet must be present exactly once.

For example, if 'a' is encrypted to 'q', then every time 'a' appears in the plaintext, it will be replaced by 'q' in the ciphertext.

Example Key:

Plain Alphabet: abcdefghijklmnopqrstuvwxyz

Cipher Key: qwertyuiopasdfghjklzxcvbnm

Using this key, the message "hello world" would be encrypted to "itssg vgksr".

Features
Encrypt: Transform plaintext into ciphertext using a provided key.

Decrypt: Revert ciphertext back to the original plaintext using the same key.

Cross-platform: Written in Python, it runs on any system with Python installed.

Getting Started

Prerequisites

Python 3.x

Usage

To use the tool, simply run the Python script from your terminal. The program will prompt you to enter the text you wish to encrypt.

python MonoalphabeticCipher.py

Code Breakdown

The script is divided into three main functions and an execution block that ties them together.

generate_key_mapping()
This function is responsible for creating the substitution key.

def generate_key_mapping():
    import string
    plain = string.ascii_uppercase
    cipher = "QWERTYUIOPASDFGHJKLZXCVBNM"
    return dict(zip(plain, cipher)), dict(zip(cipher, plain))

It defines the plain alphabet (A-Z) and a hardcoded cipher alphabet.

It uses zip() and dict() to create two dictionaries (or "maps"):

key_map: Maps each plain letter to its corresponding cipher letter (for encryption).

reverse_key_map: Maps each cipher letter back to its plain letter (for decryption).

It returns both dictionaries.

encrypt(plaintext, key_map)
This function handles the encryption process.

def encrypt(plaintext, key_map):
    result = ""
    for char in plaintext.upper():
        if char.isalpha():
            result += key_map[char]
        else:
            result += char
    return result

It takes the plaintext message and the key_map as input.

It iterates through each character of the message (converted to uppercase).

If a character is a letter, it looks up its substitution in the key_map and appends it to the result.

If a character is not a letter (e.g., a space, number, or punctuation), it is left unchanged.

decrypt(ciphertext, reverse_key_map)
This function handles decryption.

def decrypt(ciphertext, reverse_key_map):
    result = ""
    for char in ciphertext.upper():
        if char.isalpha():
            result += reverse_key_map[char]
        else:
            result += char
    return result

It works similarly to the encrypt function but uses the reverse_key_map.

It iterates through the ciphertext, looks up each letter in the reverse_key_map to find the original letter, and appends it to the result.

Main Execution
This is the part of the script that runs when the file is executed.

# Main Execution

plain_text = input("Enter Plain Text: ")
key_map, reverse_key_map = generate_key_mapping()

cipher_text = encrypt(plain_text, key_map)
print("Encrypted Text:", cipher_text)

decrypted_text = decrypt(cipher_text, reverse_key_map)
print("Decrypted Text:", decrypted_text)

It prompts the user to enter a message.

It calls generate_key_mapping() to get the encryption and decryption keys.

It calls encrypt() to encrypt the user's message and prints the result.

It then immediately calls decrypt() on the newly created ciphertext to demonstrate that the process is reversible and prints the original message.
