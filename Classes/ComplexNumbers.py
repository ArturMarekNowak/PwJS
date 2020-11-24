import math

class Complex(object):
    
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y 
    
    def __add__(self, rhs):
        newX = self.x + rhs.x
        newY = self.y + rhs.y
        return Complex(newX, newY)
    
    def __sub__(self, rhs):
        newX = self.x - rhs.x
        newY = self.y - rhs.y
        return Complex(newX, newY)
    
    def __mul__(self, rhs):
        newX = self.x * rhs.x - self.y * rhs.y 
        newY = rhs.x * self.y + rhs.y * self.x
        return Complex(newX, newY)

    def __truediv__(self, rhs):
        reNumerator = self.x * rhs.x + self.y * rhs.y 
        imNumerator = rhs.x * self.y - self.x * rhs.y
        denumerator = rhs.x**2 + rhs.y**2
        return Complex(reNumerator/denumerator, imNumerator/denumerator)

    def modulus(self):
        return (self.x**2 + self.y**2)**(1/float(2))

    def angle(self):
        fraction = self.y/self.x
        return math.degrees(math.atan(fraction))
    
    def display(self):
        print("%.5f + %.5fj" % (self.x, self.y))

print("Declare 3 complex numbers")
a = Complex(-2)
b = Complex(1, 1)
c = Complex()
print("a: ", end = '')
a.display()
print("b: ", end = '')
b.display()
print("c: ", end = '')
c.display()

print(20 * "--")
print("a + b")
c = a + b
c.display()

print(20 * "--")
print("a - b")
c = a - b
c.display()

print(20 * "--")
print("a * b")
c = a * b
c.display()

print(20 * "--")
print("a / b")
c = a / b
c.display()

print(20 * "--")
print("|b|")
print(b.modulus())

print(20 * "--")
print("angle(b)")
print(b.angle())


