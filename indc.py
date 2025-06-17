# from math import log10, comb

# def solution(n):
#     N = 2 * n
#     A = [0.5 ** N]
#     for i in range(1, N + 1):
#         numSame = N - i
#         prob = round(comb(N, numSame) * (0.5 ** numSame)  * (0.5 ** (N - numSame)), 4)
#         A.append(A[-1] + prob)
#     A = [round(log10(x), 4) for x in A]
#     A.reverse()
#     print(*A)

# solution(41)

import numpy as np
from math import factorial

n = 46

p = 0.5
# n = 5
Pr = 0
A = []
for k in range(2*n, 0, -1):
    Pr += factorial(2*n)/(factorial(k)*factorial(2*n-k)) * np.power(p,k)*np.power(1-p, 2*n-k)
    A.append(round(np.log10(Pr), 3))
for i in A[::-1]:
    print(i, end=" ")
