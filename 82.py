def func(x, k):
    a = x
    b = k
    result = list(set(a) & set(b))
    result.sort(reverse=True)
    tuple(result)
    return result

if __name__ == '__main__':
    x = list(map(int, input().split()))
    k = list(map(int, input().split()))
    result = func(x, k)
    print(*result)
