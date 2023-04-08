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
