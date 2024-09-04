def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_message += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message, shift):
    return encrypt(message, -shift)

def main():
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt a message? (E/D): ").upper()
        if choice not in ['E', 'D']:
            print("Invalid choice. Please select 'E' for encryption or 'D' for decryption.")
            continue

        message = input("Enter the message: ")
        try:
            shift = int(input("Enter the shift value: "))
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
            continue

        if choice == 'E':
            result = encrypt(message, shift)
            print(f"Encrypted message: {result}")
        else:
            result = decrypt(message, shift)
            print(f"Decrypted message: {result}")

        another = input("Do you want to process another message? (Y/N): ").upper()
        if another != 'Y':
            break

if __name__ == "__main__":
    main()
