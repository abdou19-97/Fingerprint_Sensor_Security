import re
import pickle
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.backends import default_backend


message = ''

with open('fingerprint_db.txt', 'r') as file:
    # read all the lines and add to list
    lines = file.readlines()
    
    # retrieve a specific line
    line_number = 1
    retrieved_line = lines[line_number - 1]
    
    # receive the message
    message = retrieved_line

# use reg exp to retrieve only the fingerprint characterisitics
# create a large number for the fingerprint by concatenating the entire list of characteristics
# when comparing the decryption, compare the number and the length of the number
#fingerprint_data = message.replace(",", "").replace("[", "").replace("]", "").replace(" ", "")

fingerprint_data = re.findall("\[(.*?)\]", message)
#fingerprint_data = fingerprint_data[0].split(',')
finger_concat = "".join([str(x) for x in fingerprint_data]).replace(" ", "").replace(",", "")
print(finger_concat)


# load public key from file or generate it
with open("public_key.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )


serialized_data = pickle.dumps(finger_concat)

# encrypt the serialized data
encrypted_data = public_key.encrypt(
    serialized_data,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA512()),
        algorithm=hashes.SHA512(),
        label=None
    )
)

print(encrypted_data)
