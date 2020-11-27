import random

arrayA = []
arrayB = []

def printMatrix(arr):
    for i in range (8 * 8): 
        if (((i + 1) % 8 == 0) and (i != 0)): 
            print("%d " % arr[i])
        else:
            print("%d " % arr[i], end = '')

def multiplyMatrixes(arr1, arr2):
    arrayC = []
    accumulator = 0
    for i in range(8):
        for j in range(8):
            for k in range(8):
                a = k + i * 8
                b = j + 8 * k
                accumulator += arr1[a] * arr2[b] 
            arrayC.append(accumulator)
            accumulator = 0
    return arrayC

for i in range(8 * 8):
    n = random.randint(0, 1)
    m = random.randint(0, 1)
    arrayA.append(n)
    arrayB.append(m)

print("Matrix A:")
printMatrix(arrayA)
print(20 * "-")
print("Matrix B:")
printMatrix(arrayB)
print("Matrix A*B:")
arrayC = multiplyMatrixes(arrayA, arrayB)
printMatrix(arrayC)
    


