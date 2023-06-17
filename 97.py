while True:
    try:
        u = input().strip().split(',')
        if len(u)==3:
            b = str(u[1]).split(':')
            e = str(u[2]).split(':')
            t = (int(e[0])-int(b[0]))*60 + (int(e[1])= int(b[1]))
            if t >= 60:
                h = t//60
                m = t%60
                print(u[0], f'(h:02d):(m:02d)')
        except EOFError:
            break
