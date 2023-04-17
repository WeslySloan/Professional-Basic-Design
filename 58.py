n = int(input())

a = 0
b = 0
c = 0

for i in range (1, n+1 ):
    if i%3 == 0:
        a += 1
    if i%5 == 0:
        b += 1
    if i%15 == 0:
        c += 1

print(a,b,c)
