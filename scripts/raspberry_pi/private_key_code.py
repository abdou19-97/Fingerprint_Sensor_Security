# Serialize the private key
private_key_bytes = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Save the serialized private key to a file
with open("private_key.pem", "wb") as f:
    f.write(private_key_bytes)
    

# OPEN PRIVATE KEY IN ANOTHER PROGRAM: 
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# Load the serialized private key from a file
with open("private_key.pem", "rb") as f:
    private_key_bytes = f.read()

# Deserialize the private key
private_key = serialization.load_pem_private_key(
    private_key_bytes,
    password=None
)
