def check(x, a):
    r = []
    for i in range(len(x)):
        if x[i] == a:
            r.append(i)
    return r

if __name__ == '__main__':
    d = input().split()
    r = check(d[0], d[1])
    print(r)
