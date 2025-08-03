def generate_key_mapping():
    import string
    plain = string.ascii_uppercase
    cipher = "QWERTYUIOPASDFGHJKLZXCVBNM"
    return dict(zip(plain, cipher)), dict(zip(cipher, plain))

def encrypt(plaintext, key_map):
    result = ""
    for char in plaintext.upper():
        if char.isalpha():
            result += key_map[char]
        else:
            result += char
    return result

def decrypt(ciphertext, reverse_key_map):
    result = ""
    for char in ciphertext.upper():
        if char.isalpha():
            result += reverse_key_map[char]
        else:
            result += char
    return result

# Main Execution
plain_text = input("Enter Plain Text: ")
key_map, reverse_key_map = generate_key_mapping()

cipher_text = encrypt(plain_text, key_map)
print("Encrypted Text:", cipher_text)

decrypted_text = decrypt(cipher_text, reverse_key_map)
print("Decrypted Text:", decrypted_text)
