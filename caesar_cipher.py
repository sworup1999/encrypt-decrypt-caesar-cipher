# Caesar Cipher Program by Sworup Kumar Sahu

def caesar_cipher(text, shift, operation='encrypt'):
    result = ''
    for char in text:
        if char.isalpha():
            # Determine ASCII offset for uppercase or lowercase letters
            offset = 65 if char.isupper() else 97
            # Perform shift operation for encryption or decryption
            if operation == 'encrypt':
                shifted_char = chr((ord(char) + shift - offset) % 26 + offset)
            elif operation == 'decrypt':
                shifted_char = chr((ord(char) - shift - offset) % 26 + offset)
            result += shifted_char
        else:
            # Non-alphabet characters remain unchanged
            result += char
    return result

def main():
    print("Welcome to the Caesar Cipher Program by Sworup Kumar Sahu")
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (1-25): "))

    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt the message? ").lower()
        if choice in ('e', 'd'):
            operation = 'encrypt' if choice == 'e' else 'decrypt'
            output = caesar_cipher(message, shift, operation)
            print(f"\nThe {operation}ed message is: {output}\n")
            break
        else:
            print("Invalid choice, please enter 'e' to encrypt or 'd' to decrypt.")

if __name__ == "__main__":
    main()
