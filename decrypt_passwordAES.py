#!/usr/bin/python3
from itertools import product
from Crypto.Cipher import AES
import Crypto.Cipher.AES

IV = b"\x01\x00\x01\x00\x67\x24\x4F\x43\x6E\x67\x62\xF2\x5E\xA8\xD7\x04"
key = b"\x06\x02\x00\x00\x00\xa4\x00\x00\x52\x53\x41\x31\x00\x04\x00\x00"

decipher = AES.new(key, AES.MODE_CBC, IV)

ciphertext = bytes([INSERTBYTES])

plaintext = decipher.decrypt(ciphertext).decode()

print(plaintext)
