def length(my_list):
    f = {}
    for item in my_list:
        f[item]=len(item)
    return f

if __name__ == '__main__':
    a_list = input().split()
    c = length(a_list)
    index = sorted(c.keys(), reverse=True)
    for i in index:
        print(f"{i} : {c[i]}")
