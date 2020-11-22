from liczby_zespolone import Complex
import re

q = 0

while q == 0: 
    #Information
    print("Podaj rownianie w postaci: ((znak)Re(z1)(znak)Im(z1)j)operator((znak)Re(z2)(znak)Im(z2)j)")
    
    #Capture input
    equation = input()
    
    #Ignore spaces
    equation = equation.replace(" ", "")        
    
    #Get two complex numbers parentheses
    twoNumbers = re.findall('\(([^)]+)', equation) 
    
    #
    operator = re.findall('\)([^(]+)', equation)
    
    reIm = []
    for i in range(2):
        reIm += re.findall(r'[-+]\w+', twoNumbers[i]) 

    a = reIm[0]
    b = reIm[1]
    c = reIm[2]
    d = reIm[3]
    
    a = a.replace("+", "")
    b = b.replace("j", "")
    b = b.replace("+", "")
    c = c.replace("+", "")
    d = d.replace("j", "")
    d = d.replace("+", "")
    
    a = float(a)
    b = float(b)
    c = float(c)
    d = float(d)
    
    e = Complex(a, b)
    f = Complex(c, d)

    e.display()
    f.display()
    
    g = Complex()

    if operator[0] == '+':
        g = e + f
        g.display()
    elif operator[0] == '-':
        g = e - f 
        g.display()
    elif operator[0] == '*':
        g = e * f
        g.display()
    elif operator[0] == '/':
        g = e / f
        g.display()
    else: 
        print("Cos sie popuslo")


    print("Again? [y/n]: ")
    decision = input()
    if decision == "y":
        pass
    elif not decision: 
        pass
    elif decision == "n":
        q = 99 
    else:
        print("Incorrect command") 


print("Hope to see you again!")
