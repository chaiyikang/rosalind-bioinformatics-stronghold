from functools import cache

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

@cache
def naive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return naive(n - 1) + naive(n - 2)

print(naive(400))