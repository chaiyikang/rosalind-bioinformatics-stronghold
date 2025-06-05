def solution(n, m):
    if n == 1 or n == 2:
        return 1
    memo = [[1] + [0 for _ in range(m - 1)], [0, 1] + [0 for _ in range(m - 2)]]
    for i in range(2, n, 1):
        curr = [sum(memo[i - 1]) - memo[i - 1][0]] + [memo[i - 1][j] for j in range(m - 1)]
        memo.append(curr)
    print(memo)
    return sum(memo[-1])
print(solution(88, 20))