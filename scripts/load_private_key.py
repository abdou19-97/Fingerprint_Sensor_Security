from cryptography.hazmat.primitives import serialization

# open the private key file from serialization
with open('private_key.pem', 'rb') as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None
    )
