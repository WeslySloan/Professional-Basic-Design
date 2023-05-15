def count(x):
    n = x.count(x[0])
    c= x[0]
    for i in range(1, len(x)):
        if x.count(x[i]) > n:
            n= x.count(x[i])
            c = x[i]
        elif x.count(x[i]) == n:
            if c < x[i]:
                c = x[i]
        else:
            pass
    return c, n

if __name__ == '__main__':
    d = list(input())
    c, n = count(d)
    print(f"{c:s} {n:d}")
