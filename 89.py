def mode(a):
    f = {}
    for i in a:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1

    m = max(f.values())
    c = [k for k,v in f.items() if m==v]
    if len(c) == len(f.keys()) and len(c) != 1:
        return []
    else:
        return c

if __name__ == '__main__':
    a = list(map(int, list(input().split())))
    c = mode(a)
    if len(c) == 0:
        print("None")
    else:
        c.sort()
        for i in c:
            print(i, end=" ")
