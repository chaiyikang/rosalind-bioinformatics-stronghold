def fib(n):
    # return 0 if n == 0 else 1 if n == 1 else fib(n - 1) + fib(n - 2)
    if n == 0:
        return 0
    if n == 1:
        return 1
    a = 0
    b = 1
    for i in range(2, n + 1, 1):
        tmp = a
        a = b
        b = tmp + a
    return b

print(fib(23))