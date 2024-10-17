def encrypt(string, shift):
    # Program 3: Caesar Cipher
    # Initialize an empty string to store the encrypted message
    cipher = ''
    for char in string:
        if char == ' ':
            # Keep spaces unchanged
            cipher += char
        elif char.isupper():
            # Encrypt uppercase letters
            cipher += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            # Encrypt lowercase letters
            cipher += chr((ord(char) + shift - 97) % 26 + 97)
    return cipher

def decrypt(string, shift):
    # Initialize an empty string to store the decrypted message
    cipher = ''
    for char in string:
        if char == ' ':
            # Keep spaces unchanged
            cipher += char
        elif char.isupper():
            # Decrypt uppercase letters
            cipher += chr((ord(char) + (26 - shift) - 65) % 26 + 65)
        else:
            # Decrypt lowercase letters
            cipher += chr((ord(char) + (26 - shift) - 97) % 26 + 97)
    return cipher

# Get user input
text = input("Enter String: ")
s = int(input("Enter Shift Number: "))
option = int(input("1. For Encrypt\n2. For Decrypt\nEnter your choice: "))

# Display the original string
print("Original String:", text)

if option == 1:
    # Encrypt the text
    print("After Encryption:", encrypt(text, s))
else:
    # Decrypt the text
    print("After Decryption:", decrypt(text, s))