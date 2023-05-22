def freq(my_list):
    f  = {}
    for item in my_list:
        if  (item in f):
            f[item] += 1
        else:
            f[item] = 1
    return f

if __name__ == '__main__':
     a = list(map(int, list(input().split())))
     c = freq(a)
     index = sorted(c.keys())
     for i in index:
         print(f"{i} : {c[i]}")
