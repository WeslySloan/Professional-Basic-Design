result=[]
b = 0
i = 0

def func(numbers):
    for i in range(len(number)):
    b = number[i] + b
    result.append(b)

    return b

number = list(map(int,input().split()))

result = func(number)

print(*result)
