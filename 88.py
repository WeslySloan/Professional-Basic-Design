def dup(a):
    f = {}
    s = set()
    for i in a:
        if i in f:
            f[i] += 1
        else:
            f[i] = 1
    for k,v in f.items():
        if v >= 2:
            s.add(k)
    return s

if __name__ == '__main__':
    a = list(map(int, list(input().split())))
    s = dup(a)
    if len(s) != 0:
        l = list(s)
        l.sort()
        for i in l:
            print(i, end=" ")
    else:
        print("None")
