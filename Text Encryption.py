import string
from cryptography.fernet import Fernet

def caesar_encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shifted_char = chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift) % 26 + 97)
            encrypted_message += shifted_char
        else:
            encrypted_message += char
    return encrypted_message

def caesar_decrypt(encrypted_message, shift):
    decrypted_message = ""
    for char in encrypted_message:
        if char.isalpha():
            shifted_char = chr((ord(char) - 65 - shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 - shift) % 26 + 97)
            decrypted_message += shifted_char
        else:
            decrypted_message += char
    return decrypted_message

def generate_vigenere_table():
    table = []
    for i in range(26):
        table.append([])
        for j in range(26):
            table[i].append(chr(((i + j) % 26) + 65))
    return table
    
def vigenere_encrypt(message, key):
    table = generate_vigenere_table()
    cipher_text = ""
    key = key.upper()
    key_index = 0

    for char in message:
        if char.isalpha():
            shift = ord(key[key_index]) - 65
            cipher_text += table[ord(char.upper()) - 65][shift]
            key_index = (key_index + 1) % len(key)
        else:
            cipher_text += char

    return cipher_text

def vigenere_decrypt(message, key):
    table = generate_vigenere_table()
    plain_text = ""
    key = key.upper()
    key_index = 0

    for char in message:
        if char.isalpha():
            shift = ord(key[key_index]) - 65
            row_index = ord(char.upper()) - 65
            col_index = table[row_index].index(char.upper())
            plain_text += chr((col_index - shift) % 26 + 65)
            key_index = (key_index + 1) % len(key)
        else:
            plain_text += char

    return plain_text

def generate_cipher_mapping(key):
    alphabet = string.ascii_lowercase
    cipher_mapping = {}
    for i in range(len(alphabet)):
        cipher_mapping[alphabet[i]] = key[i]
    return cipher_mapping

def substitution_encrypt(message, key1):
    encrypted_message = ''
    for char in message:
        if char.lower() in key1:
            encrypted_message += key1[char.lower()]
        else:
            encrypted_message += char
    return encrypted_message
def substitution_decrypt(message, key1):
    decryption_mapping = {v: k for k, v in key1.items()}
    decrypted_message = ''
    for char in message:
        if char.lower() in decryption_mapping:
            decrypted_message += decryption_mapping[char.lower()]
        else:
            decrypted_message += char
    return decrypted_message

def railfence_encrypt(message, key):
    fence = [['\n' for i in range(len(message))] for j in range(key)]
    direction = -1
    row, col = 0, 0

    for char in message:
        if row == 0 or row == key- 1:
            direction *= -1
        fence[row][col] = char
        col += 1
        row += direction

    cipher_text = ''.join([item for sublist in fence for item in sublist if item != '\n'])
    return cipher_text


def railfence_decrypt(message, key):
    fence = [['\n' for i in range(len(message))] for j in range(key)]
    direction = -1
    row, col = 0, 0

    for char in message:
        if row == 0 or row == key - 1:
            direction *= -1
        fence[row][col] = '*'
        col += 1
        row += direction
    
    index = 0
    for i in range(key):
        for j in range(len(message)):
            if fence[i][j] == '*' and index < len(message):
                fence[i][j] = message[index]
                index += 1

    direction = -1
    row, col = 0, 0
    plain_text = ''

    for i in range(len(message)):
        if row == 0 or row == key - 1:
            direction *= -1
        plain_text += fence[row][col]
        col += 1
        row += direction

    return plain_text

def transposition_encrypt(message, key):
    while len(message) % key != 0:
        message += ' '

    grid = ['' for _ in range(key)]
    for i, char in enumerate(message):
        grid[i % key] += char

    ciphertext = ''.join(grid)
    return ciphertext

def transposition_decrypt(message, key):
       
    cols = len(message) // key

    grid = ['' for _ in range(cols)]
    for i, char in enumerate(message):
        grid[i // cols] += char

    plaintext = ''.join(grid)
    return plaintext.strip() 

def main():
    key = 'zyxwvutsrqponmlkjihgfedcba'
    key1 = generate_cipher_mapping(key)
    while True:
        print("Choose an encryption technique:")
        print("1. Caesar Cipher Encrypt")
        print("2. Caesar Cipher Decrypt")
        print("3. Vigenère Cipher Encrypt")
        print("4. Vigenère Cipher Decrypt")
        print("5. Substitution Cipher Encrypt")
        print("6. Substitution Cipher Decrypt")
        print("7. Railfence Cipher Encrypt")
        print("8. Railfence Cipher Decrypt")
        print("9. Transposition Cipher Encrypt")
        print("10. Transposition Cipher Encrypt")
        print("11. Quit")

        choice = input("Enter your choice: ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_encrypt(message, shift)
            print("Encrypted message:", encrypted_message)

        elif choice == '2':
            encrypted_message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = caesar_decrypt(encrypted_message, shift)
            print("Decrypted message:", decrypted_message)

        elif choice == '3':
            message = input("Enter the plain text: ")
            key = input("Enter the encryption key: ")
            encrypted_text = vigenere_encrypt(message, key)
            print("Encrypted message:", encrypted_text)

        elif choice == '4':
            message = input("Enter the cipher text: ")
            key = input("Enter the decryption key: ")
            decrypted_text = vigenere_decrypt(message, key)
            print("Decrypted message:", decrypted_text)
            

        elif choice == '5':
            message = input("Enter the message to encrypt: ")
            encrypted_message = substitution_encrypt(message, key1)
            print("Encrypted message:", encrypted_message)
       
        elif choice == '6':
            encrypted_message = input("Enter the message to decrypt: ")
            decrypted_message = substitution_decrypt(encrypted_message, key1)
            print("Decrypted message:", decrypted_message)
       
        elif choice == '7':
            plain_text = input("Enter the message to encrypt: ")
            rails = int(input("Enter the number of rails: "))
            cipher_text = railfence_encrypt(plain_text, rails)
            print("Encrypted text:", cipher_text)
            
        elif choice == '8':
            cipher_text = input("Enter the message to decrypt: ")
            rails = int(input("Enter the number of rails: "))
            plain_text = railfence_decrypt(cipher_text, rails)
            print("Decrypted text:", plain_text)

        elif choice == '9':
            message = input("Enter the message to encrypt: ")
            key = int(input("Enter the encryption key: "))
            ciphertext =transposition_encrypt(message, key)
            print("Encrypted message:", ciphertext)
        
        elif choice == '10':
            ciphertext = input("Enter the message to decrypt: ")
            key = int(input("Enter the decryption key: "))
            plaintext = transposition_decrypt(ciphertext, key)
            print("Decrypted message:", plaintext)

        elif choice == '11':
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
