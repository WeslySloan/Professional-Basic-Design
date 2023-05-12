from itertools import accumulate

def func(numbers):
    return list(accumulate(numbers))

numbers = list(map(int, input().split()))
result = func(numbers)
print(*result)
