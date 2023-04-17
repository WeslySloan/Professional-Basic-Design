dice = input().split(",")

n = len(dice)
total = 0

for i in range(n):
    total += int(dice[i])

avg = total / n

print(n, total, format(avg, ".1f"))
