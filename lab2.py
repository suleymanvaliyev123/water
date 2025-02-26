x = 3
Z =[]
a = int (input ("enter the number a:"))
while x <= 7:
    if a*x > 20:
        z = 2*x**2 + 3*a
    else:
        z = 4*a**2 - 3*x 
    x += 0.5
    Z.append(z)
print(Z)
