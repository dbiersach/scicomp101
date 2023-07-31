# caesar_decrypt_2.py

import numpy as np

file_name = "ciphertext2.txt"
key_shift = -154

f_in = open(file_name, "rb")
f_bytes = bytearray(f_in.read())

for i in np.arange(len(f_bytes)):
    f_bytes[i] = (f_bytes[i] + key_shift) % 256

print(f_bytes.decode("utf-8", "ignore"))
