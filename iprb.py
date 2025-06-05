def solution(k, m, n):
    total = k + m + n
    mateCombinations = total * (total - 1)

    # AA x ??
    o1 = k * (total - 1)
    
    o2 = m * (k + 0.75 * (m - 1) + 0.5 * n)

    o3 = n * (k + 0.5 * m)

    return (o1 + o2 + o3) / mateCombinations

print(solution(27, 24, 17))