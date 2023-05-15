def find(x, a):
    c = []
    for i in range(len(x)):
        if x[i][0].lower() == a.lower():
            c.append(x[i])
    return c

if __name__ == '__main__':
    a = input().strip()
    d = list(input().split())
    c = find(d, a)
    for i in range(len(c)) :
        print(c[i])
