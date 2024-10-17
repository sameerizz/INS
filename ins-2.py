# Program 2: RSA Encryption and Decryption
# Import necessary libraries
# pip install pycryptodome
from Crypto.PublicKey import RSA  # For RSA key generation and management
from Crypto.Cipher import PKCS1_OAEP  # For PKCS#1 OAEP encryption
import binascii  # For hexadecimal conversion

# Generate RSA key pair (public and private key)
keyPair = RSA.generate(1024)  # Generate a 1024-bit RSA key pair

# Get the public key from the key pair
pubKey = keyPair.publickey()

# Print the public key components: modulus (n) and exponent (e)
print(f"Public key: (n={hex(pubKey.n)}, e={hex(pubKey.e)})")

# Export the public key in PEM format and print it
pubKeyPEM = pubKey.export_key()
print(pubKeyPEM.decode('utf-8'))

# Print the private key components: modulus (n) and private exponent (d)
print(f"Private key: (n={hex(keyPair.n)}, d={hex(keyPair.d)})")

# Export the private key in PEM format and print it
privKeyPEM = keyPair.export_key()
print(privKeyPEM.decode('utf-8'))

# Message to be encrypted (convert the string to bytes)
msg = b'Hello Class!'  # Define the message as bytes

# Encrypt the message using the public key and PKCS1_OAEP
encryptor = PKCS1_OAEP.new(pubKey)  # Create a new PKCS1_OAEP cipher object with the public key
encrypted = encryptor.encrypt(msg)  # Encrypt the message

# Print the encrypted message in hexadecimal format
print("Encrypted:", binascii.hexlify(encrypted).decode('utf-8'))  # Convert to hex and then to string for printing
