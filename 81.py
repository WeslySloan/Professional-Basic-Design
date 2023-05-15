def func(x, k):
    c = tuple(k)
    result = c.count(x)
    return result

if __name__ == '__main__':
    x = int(input())
    k = list(map(int, input().split()))
    result = func(x, k)
    print(result)
