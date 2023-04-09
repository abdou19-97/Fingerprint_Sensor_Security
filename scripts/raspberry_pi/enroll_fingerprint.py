import hashlib
from pyfingerprint.pyfingerprint import PyFingerprint
from pyfingerprint.pyfingerprint import FINGERPRINT_CHARBUFFER1

# Try to initialize the sensor
try:
    f = PyFingerprint('/dev/ttyS0', 57600, 0xFFFFFFFF, 0x00000000)

    if ( f.verifyPassword() == False ):
        raise ValueError('The given fingerprint sensor password is wrong!')

except Exception as e:
    print('The fingerprint sensor could not be initialized!')
    print('Exception message: ' + str(e))
    exit(1)

print('Currently stored templates: ' + str(f.getTemplateCount()))

# enroll a new fingerprint
print('Waiting for finger...')
while(f.readImage() == False):
    pass

# convert the image to finger characterisitics
# and store it in the sensor's buffer memory
f.convertImage(0x01)

# ask the user to input an id for the new fingerprint
id = input('Enter ID (must be a number): ')

# check if the ID is already used
result = f.searchTemplate()
if (result[0] >= 0):
    print('This ID already exists. Try again with a different ID.')
    exit(0)

# create a text file and store the ID and characteristics
filename = 'fingerprint_db.txt'
with open(filename, 'a') as file:
    file.write(str(id) + ',' + str(f.downloadCharacteristics()) + '\n')
    
# store the characteristics into the sensor's flash memory
f.storeTemplate()
print('fingerprint enrolled successfully')
