a = [
    3,5,3,
    1,2,3,
    6,7,0
]
cem = 0
i = 0
n = len(a)
k = int(n ** 0.5) + 1
while i<=(n-1):
    cem = cem + a[i]
    i = i + k 
print(cem)


