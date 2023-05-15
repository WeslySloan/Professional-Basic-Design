def positive_sum(numbers):
    result = 0
    for num in numbers:
        if num > 0:
            result += num
    return result

numbers = list(map(int, input().split(',')))
result = positive_sum(numbers)
print("Sum = ", result)
