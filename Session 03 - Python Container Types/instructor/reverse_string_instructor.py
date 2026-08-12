#!/usr/bin/env -S uv run
"""reverse_string_instructor.py"""

s1 = "Forever Young"
print(s1)

s2 = ""
for i in range(len(s1) - 1, -1, -1):
    s2 += s1[i]
print(s2)  # Output: gnuY reverof

s3 = ""
for c in s1:
    s3 = c + s3
print(s3)  # Output: gnuY reverof

print(s1[::-1])  # Output: gnuY reverof
