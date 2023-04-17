a = input().split(' ')

won = int(a[0])

for i in range(1, int(a[2])+1):
               print(f"{i:d} {won:10.0f} won")
               won *= (1.0 - float(a[1])/100.0)
