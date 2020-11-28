import threading, queue
import random 
import matplotlib.pyplot as plt
import matplotlib.spines
import time

data = []
y = []
x = []
x = list(range(1, 26))

for i in range(5000):
    temp = random.gauss(100, 50)
    data.append(temp)

def foo(data, num):
    
    c1 = 0 
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    
    for i in range(len(data)):
        if (data[i] >= (-62.5 + 62.5 * num) and (data[i] < (-50 + 62.5 * num))):
            c1 += 1
        elif (data[i] >= (-50 + 62.5 * num) and data[i] < (-37.5 + 62.5 * num)):
            c2 += 1
        elif (data[i] >= (-37.5 + 62.5 * num) and data[i] < (-25 + 62.5 * num)):
            c3 += 1
        elif (data[i] >= (-25 + 62.5 * num) and data[i] < (-12.5+ 62.5 * num)):
            c4 += 1
        elif (data[i] >= (-12.5 + 62.5 * num) and data[i] < (0 + 62.5 * num)):
            c5 += 1
    
    

    y.append(c1)
    y.append(c2)
    y.append(c3)
    y.append(c4)
    y.append(c5)

t0 = threading.Thread(target = foo, args=(data, 0))
t1 = threading.Thread(target = foo, args=(data, 1))
t2 = threading.Thread(target = foo, args=(data, 2))
t3 = threading.Thread(target = foo, args=(data, 3))
t4 = threading.Thread(target = foo, args=(data, 4))

t0.start()
t1.start()
t2.start()
t3.start()
t4.start()

t0.join()
t1.join()
t2.join()
t3.join()
t4.join()

color = ['yellow', 'greenyellow', 'lawngreen', 'limegreen', 'g']
color = color * 5

barlist = plt.bar(x, y, color = color)

plt.show()
print("Done")



