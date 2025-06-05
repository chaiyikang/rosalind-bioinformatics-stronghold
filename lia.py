from math import pow, comb

def solution(k, n):
    # dp = [[1, 0, 0]]
    # while len(dp) < k + 1:
    #     prev = dp[-1]
    #     Aa = prev[0] * 0.5 + prev[2] * 0.5 + prev[1] * 0.5
    #     xAA = prev[0] * 0.25 + prev[1] * 0.5
    #     aa = prev[0] * 0.25 + prev[2] * 0.5
    #     dp.append([Aa, xAA, aa])
    # prob = pow(dp[k][0], 2) # consider gene B
    # above is unnecessary: notice that AA, aa, Aa when crossed with Aa will always give Aa with probability 0.5
    # so probability of Aa remains constant throughout generations
    size = int(pow(2, k))
    prob = 0.25
    totalProb = 0
    for i in range(n, size + 1):
        print(i)
        totalProb += comb(size, i) * pow(prob, i) * pow((1 - prob), size - i)
    return totalProb

print(solution(7, 34))
