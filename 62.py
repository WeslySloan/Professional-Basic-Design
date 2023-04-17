def dist (x1, y1, x2, y2):
    dx = x1-x2
    dy = y1-y2
    d = (dx*dx+dy*dy)**0.5
    return d

x1, y1 = input().split()
x2, y2 = input().split()

d = dist(int(x1), int(y1), int(x2), int(y2))

print(f"{d:.4f}")
