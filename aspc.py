from math import comb

def solution(n, m):
    summ = 0
    for k in range(m, n + 1):
        summ += comb(n, k)
        summ %= 1000000
    print(summ)

solution(1754, 1206)