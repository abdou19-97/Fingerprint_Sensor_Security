from cryptography.hazmat.primitives.asymmetric import padding

# create a fingerprint hash 
message = b"Hello, world!"

# encrypt the fingerprint hash 
encrypted_data = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# send the encrypted data to the machine that will be decrypting it
