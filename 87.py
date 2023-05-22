def trans(a):
    if a in Weeks:
        return Weeks[a]
    else:
        return "X"

Weeks  = {"Sun":"Sunday", "Mon":"Monday", "Tue":"Tuesday", "Wed":"Wednesday", "Thu":"Thursday",
        "Fri":"Friday", "Sat":"Saturday"}

if __name__ == '__main__':
    w = input().strip()
    c = trans(w)
    print(c)
