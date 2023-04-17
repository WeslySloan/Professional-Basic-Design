def fib(n):
    _curr, _next = 0, 1
    for _ in range(n + 1):
        yield _curr
        _curr, _next = _next, _curr + _next

n = int(input())
n = fib(n)
print ('{}'.format(str(n))

