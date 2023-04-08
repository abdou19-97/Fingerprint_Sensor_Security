from cryptography.hazmat.primitives.asymmetric import rsa, serialization

# generate a private key on the laptop
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# open the private key file from serialization
with open('private_key.pem', 'rb') as f:
    private_key = serialization.load_pem_private_key(
        f.read(),
        password=None
    )
