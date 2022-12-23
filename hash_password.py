import binascii
import hashlib
import os
import sys
import bcrypt

given_password = sys.argv[1]


# Cria hash para uma senha, utilizando o hashlib.
def hash_password(password, salt_len=16, iterations=10000, encoding='utf-8'):
    salt = os.urandom(salt_len)
    hashed_password = hashlib.pbkdf2_hmac(hash_name='sha256', password=bytes(password, encoding), salt=salt, iterations=iterations)
    return salt, iterations, hashed_password


hash_password(given_password)

# Utilizando bcrypt e binascii.
password = bytes('password', 'utf-8')
hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt(14))
print(hashed_pw)

# Armazenar a senha.
hexed_hashed_pw = binascii.hexlify(hashed_pw)
#store_password(user_id=42, password=hexed_hashed_pw)
#hexed_hashed_pw = retrieve_password(user_id=42)
hashed_pw = binascii.unhexlify(hexed_hashed_pw)

# Visualização.
bcrypt.hashpw(password, hashed_pw)
print(bcrypt.hashpw(password, hashed_pw) == hashed_pw)