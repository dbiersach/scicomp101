# seq_lrss.py

import re


def match(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    s3 = ""
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            s3 += s1[i]
        else:
            break
    return s3


def lrss(seq):
    # Step 1 - Form the suffixes list
    suffixes = []
    for i in range(len(seq)):
        suffixes.append(seq[i:])

    # Step 2 - Sort the suffixes list
    suffixes.sort()

    # Step 3 - Scan the suffixes list
    longest = ""
    for i in range(len(suffixes) - 1):
        s1 = suffixes[i]
        s2 = suffixes[i + 1]
        candidate = match(s1, s2)
        if len(candidate) > len(longest):
            longest = candidate

    return longest


def main(file_name):
    with open(file_name, "rb") as f_in:
        print(f"Analyzing {file_name} . . .")

        # Read in text file into an array of file bytes
        f_bytes = bytearray(f_in.read())

        # Enforce uppercase and remove non-letters, convert to UTF-8
        seq = bytearray(f_bytes).decode().upper()
        seq = re.compile("[^A-Z]").sub("", seq)

        # Find and print the longest repeated sub-string (lrss)
        longest = lrss(seq)
        print(f"Longest repeated substring: {longest} ")

        return


main("fruitfly.txt")
