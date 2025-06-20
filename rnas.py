wobbleBasePairing = {"A": set("U"), "U": set(["A", "G"]), "G": set(["C", "U"]), "C": set("G")}

def solution(input):
    seq = input
    n = len(seq)
    dp = [[None] * n for _ in range(n)]

    def helper(i, j):
        if i < 0 or j < 0 or i >= n or j >= n or i > j:
            return 1
        if dp[i][j] is not None:
            return dp[i][j]
        dontPair = helper(i + 1, j)
        complements = wobbleBasePairing[seq[i]]
        pairSum = 0
        for k in range(i + 1, j + 1):
            if seq[k] not in complements or k - i < 4:
                continue
            pairSum += helper(i + 1, k - 1) * helper(k + 1, j)
        result = dontPair + pairSum
        dp[i][j] = result
        return result
    
    return helper(0, n - 1)

print(solution('''AACGGUUGCUACAGUUAGCCUAUUGUGGCCUGCCUCUCGUAUCACUCACUUCUCGUAAUCUUAGGAGACAAGCGAGUUGUACCAAUGUAUGCCGGUGUUGAAUAGCAAUGAAACGUGUCAGCGCUGCGUAGCUUUUUUCACGAGAUCUCUAAGAAUCCGACAAGUCUGCUUUCCCCAUAACUAGCUCAGGAC'''))
