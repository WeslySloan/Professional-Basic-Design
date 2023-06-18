def func():
    d = {}
    input_list = input().split()
    for i in range(0, len(input_list), 2):
        key = input_list[i]
        value = int(input_list[i + 1])
        d[key] = value
    return sum(d.values())

if __name__ == '__main__':
    result = func()
    print(result)
