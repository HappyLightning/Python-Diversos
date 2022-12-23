import os, hashlib
import sys


given_password = sys.argv[1]

# Cria hash para uma senha, utilizando 10000 iterações.
def hash_password(password, salt_len=16, iterations=10000, encoding='utf-8'):
    salt = os.urandom(salt_len)
    hashed_password = hashlib.pbkdf2_hmac(hash_name='sha256', password=bytes(password, encoding), salt=salt, iterations=iterations)
    return salt, iterations, hashed_password

hash_password(given_password)
