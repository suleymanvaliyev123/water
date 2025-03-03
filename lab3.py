import math
y = 0
x = 0.5
f = 1
a = 1
while math.sin(a*x)/f >= 0.001:
    y = y + math.sin(a*x)/f
    f = f * a
    a += 2
print (y)
