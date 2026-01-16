# hamming_weight_instructor.py

n = 95601

c = 0
while n > 0:
    c = c + n % 2
    n = n // 2

print(c)
