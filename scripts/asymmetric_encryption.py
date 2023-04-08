from cryptography.hazmat.primitives.asymmetric import rsa

# generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# create a public key from the private key 
public_key = private_key.public_key()

# save the public key to a file
with open('public_key.pem', 'wb') as f:
    f.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

# send this public key to the computer that will be decrypting the data
