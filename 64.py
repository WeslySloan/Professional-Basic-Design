def midpoint(x1, y1, x2, y2):
    xc=(x1+x2)/2.0
    yc=(y1+y2)/2.0
    return xc, yc

if __name__ == '__main__':
    p1 = list(map(float,input().split()))
    p2 = list(map(float,input().split()))

    xc, yc = midpoint(p1[0], p1[1], p2[0], p2[1])
    print(f"{xc:.2f}, {yc:.2f}")
