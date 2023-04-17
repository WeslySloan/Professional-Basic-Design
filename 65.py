def inf_rate(i, f):
    return ((f - i) / i)*100

def avg_inf_rate(n):
    air = 0
    for i in range(n):
        i, f = map(float, input().split())
        air += inf_rate(i,f)

    return (air/n)

if __name__ == '__main__':
    n = int(input())

    print (f"Average Inflation Rate: {avg_inf_rate(n):.2f}%")
