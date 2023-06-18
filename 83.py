def sum_all(t):
    return sum(t)

if __name__ == '__main__':
    t = tuple(map(int, input().split()))
    result = sum_all(t)
    print(result)
