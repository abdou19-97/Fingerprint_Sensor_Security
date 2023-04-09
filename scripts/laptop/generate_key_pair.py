from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

# generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# get the public key from the private key
public_key = private_key.public_key()

# write the public key to a file to be sent to raspberry pi
with open('public_key.pem', 'wb') as f:
    f.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

    
    
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes

# Generate a public/private key pair
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)
public_key = private_key.public_key()

# Alice encrypts a message using Bob's public key
message = b"Hello, Bob!"
# The code shows how to configure padding for encryption
#  or decryption using the OAEP (Optimal Asymmetric Encryption Padding) scheme.
ciphertext = public_key.encrypt(
    message,
    padding.OAEP( # The padding.OAEP method initializes a new instance of the OAEP padding class.
        # mgf=padding.MGF1(algorithm=hashes.SHA256()) 
        # specifies the Mask Generation Function (MGF1), which is used to randomize the input before encryption.
        # It is set to MGF1 with SHA-256 hash function.
        mgf=padding.MGF1(algorithm=hashes.SHA256()), 
        algorithm=hashes.SHA256(), # algorithm=hashes.SHA256() specifies the hash function used in the OAEP scheme.
        label=None,
    )
   
)


# Bob decrypts the message using his private key
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None,
    )
)

print("Original message:", message)
print("Ciphertext message:",ciphertext)
print("Decrypted message:", plaintext)


# In summary, these lines of code set up an OAEP padding scheme that uses SHA-256 for both the MGF1 and OAEP hash functions and doesn't use any label.
# This padding scheme can be used to encrypt or decrypt messages.
