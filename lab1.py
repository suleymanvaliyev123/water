import math as a
n1 = a.tan(1)*((10**0.1 + 10)**0.1)
n2 = (1 + a.log(10,20)**0.2)**15
if n1 + n2 < 5:
    n3 = a.sin(a.pi*n1 + a.e**n2)
else:
    a.sin(a.pi*n1 + n2)
print(n3)
