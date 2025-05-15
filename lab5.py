a = [7,3,5,4,2,11]
product = 1
i = 0
n = len(a)
while i<=(n-1):
    if i % 2 == 1:
        product = product*a[i]
    i = i + 1
print(product) 

