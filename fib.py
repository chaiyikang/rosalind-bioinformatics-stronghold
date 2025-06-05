def solution(n, k):
    if n == 0 or n == 1:
        return 1
    a = 1
    b = 1
    for i in range(n - 2):
        tmp = a
        a = b
        b = k * tmp + b
    return b
print(solution(29, 4))