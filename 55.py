a = int(input())
b = float(input())
c = int(input())

total = a

for i in range(c):
    total += total * b / 100.0
print (format(total, ".0f"))


