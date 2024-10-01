from cryptography.fernet import Fernet

# we will encrypt the below string
message = "hello geeks"

# generate a key for encryption and decryption 
# You can use fernet to geenrate 
# the key or use random key generator 
# here I'm using fernet to genrate key 

key = Fernet.generate_key()

# Instance the Fernet class with the key

fernet = Fernet(key)

# then use the fernet class instance 
# to encrypt the string string must
# be encoded the to byte string before encryption 
encMessage = fernet.encrypt(message.encode())

print("Orginal String:", message)
print("Encrypted String:", encMessage)

# decrypt the encrypted string with the 
# Fernet instance of the key
# that was used to for encrypting the string 
# encoding byte string is returned by decryoted method 
# so decode it to string with decoded methods 
decMessage = fernet.decrypt(encMessage).decode()

print("decrypted string:", decMessage)


