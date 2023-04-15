from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.primitives.serialization import load_pem_private_key

# 1. Generate a symmetric encryption key using a secure random generator:
key = Fernet.generate_key()

# 2. Encrypt the fingerprint data using the symmetric key
with open('fingerprint.txt', 'rb') as f:
    data = f.read()

f = Fernet(key)
encrypted_data = f.encrypt(data)

# 3. Load the recipient's public key from a file
with open("public_key.pem", "rb") as key_file:
    public_key = load_pem_public_key(key_file.read())

# 4. Use the recipient's public key to encrypt the symmetric key
encrypted_key = public_key.encrypt(
    key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# 5. Send the encrypted data and encrypted key to the recipient.
with open("private_key.pem", "rb") as key_file:
    private_key = load_pem_private_key(
        key_file.read(),
        password=None
    )

# 6. The recipient uses their private key to decrypt the encrypted symmetric key
key = private_key.decrypt(
    encrypted_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# 7. The recipient uses the decrypted symmetric key to decrypt the data
f = Fernet(key)
decrypted_data = f.decrypt(encrypted_data)

# 8. Save the decrypted fingerprint data to a file
with open('decrypted_fingerprint.txt', 'wb') as f:
    f.write(decrypted_data)


 with open('encrypted_fingerprint.txt', 'wb') as f:
    f.write(encrypted_data)
