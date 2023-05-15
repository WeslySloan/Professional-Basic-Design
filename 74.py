def calc(x):
    x.sort()
    s = 0
    for i in range(1,len(x)-1):
        s += x[i]
    a = s/(len(x)-2)
    return s, a

if __name__ == '__main__':
    d = map(int,input().split())
    d = list(d)
    s, a = calc(d)
    print(f"Sum = {s:d}, Average = {a:.1f}")
