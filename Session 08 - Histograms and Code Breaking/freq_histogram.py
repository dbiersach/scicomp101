# freq_histogram.py

import numpy as np
import matplotlib.pyplot as plt
import collections
import pathlib

file_name = "gettysburg.txt"
# file_name = "ciphertext1.txt"

# Read the data file into a buffer
f_in = open(file_name, "rb")
f_bytes = bytearray(f_in.read())
f_in.close()

# Only set tick marks for characters that occur more than 6%
ticks = []
char_count = np.zeros(256)
for char, count in collections.Counter(f_bytes).items():
    char_count[char] = count
    if count / len(f_bytes) > 0.06:
        ticks.append(char)

# Create a histogram of each character's ASCII value
plt.figure(pathlib.Path(__file__).name)
plt.bar(np.arange(256), char_count)
plt.xticks(ticks)
plt.tick_params("x", rotation=90)
plt.title(f"Frequency Analysis ({file_name})")
plt.xlabel("ASCII Value")
plt.ylabel("Count")
plt.show()
