a = [1, 2, 12, 4]
b = [2, 4, 2, 8]

accumulator = 0

for i in range(len(a)):
    accumulator += a[i] * b[i]

print(accumulator)
