def i_list(x, k):
    c = 0
    for i in range(len(x)):
        if x[i] > k:
            c = c + 1
    return c

if __name__ == '__main__':
    k = int(input())
    x = list(map(int, input().split()))
    c = i_list(x, k)
    print(c)
