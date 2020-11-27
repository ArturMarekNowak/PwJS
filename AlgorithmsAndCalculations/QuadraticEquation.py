import math 
from sys import argv

script, a, b, c = argv

a = float(a)
b = float(b)
c = float(c) 

delta = b**2 - 4 * a * c

x1 = (b**2 + delta**(1/float(2))) / (2 * a)

x2 = (b**2 - delta**(1/float(2))) / (2 * a)

print("x1: %r, x2: %r" % (x1, x2))
