import random 
arrayA = []
arrayB = []

def printArray(arr):
    for i in range(128 * 128):
        if (((i + 1) % 128 == 0) and (i != 0)):
            print("%d" % arr[i])
        else:
            print("%d" % arr[i], end = '')

def addMatrixes(arr1, arr2):
    arrayC = []
    for i in range(128 * 128):
        temp = arr1[i] + arr2[i]
        arrayC.append(temp)
        temp = 0

    return arrayC

for i in range(128 * 128):
    n = random.randint(0, 1)
    m = random.randint(0, 1)
    arrayA.append(n)
    arrayB.append(m)


printArray(arrayA)
print(50 * "-")
printArray(arrayB)
print(50 * "-")
printArray(addMatrixes(arrayA, arrayB))
