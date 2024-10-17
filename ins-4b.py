# Program 4B: RSA Digital Signature
# Import necessary modules from the PyCryptodome library
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Generate an RSA key pair (public and private keys)
key = RSA.generate(2048)  # Generates a 2048-bit RSA key pair
private_key = key.export_key()  # Export the private key
public_key = key.publickey().export_key()  # Export the public key

# Simulated document content
original_document = b"This is the original document content."  # Original document in bytes
modified_document = b"This is the modified document content."  # Modified document in bytes

# Hash the document content using SHA-256
original_hash = SHA256.new(original_document)  # Create SHA-256 hash of the original document
modified_hash = SHA256.new(modified_document)  # Create SHA-256 hash of the modified document

# Create a signature using the private key
signature = pkcs1_15.new(RSA.import_key(private_key)).sign(original_hash)
# Sign the hash of the original document using the private key

# Verify the signature using the public key with the original content
try:
    pkcs1_15.new(RSA.import_key(public_key)).verify(original_hash, signature)
    # Verify the signature of the original document's hash using the public key
    print("Signature is valid.")
except (ValueError, TypeError):
    # If verification fails, print "Signature is invalid."
    print("Signature is invalid.")
