from math import factorial

def fact(n, mod):
    if n == 0 or n == 1:
        return 1
    return (n * fact(n - 2, mod)) % mod

def solution(n):
    return fact(2 * n - 5, 1000000)


print(solution(994))