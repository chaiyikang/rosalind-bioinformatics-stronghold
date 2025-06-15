# def cat(n: int) -> int:
#     dp = [1, 1]
#     for i in range(2, n + 1):
#         sum = 0
#         for j in range(1, i + 1):
#             sum += dp[j - 1] * dp[i - j]
#         dp.append(sum)
#     print(dp)

# cat(5)

basePairing = {"A": "U", "U": "A", "G": "C", "C": "G"}

def solution(input: str) -> int:
    seq = "".join(input.splitlines()[1:])
    length = len(seq)
    pfsum = {"A": [], "G": [], "U": [], "C": []}
    
    for base in seq:
        for b in pfsum:
            if not pfsum[b]:
                pfsum[b].append(0)
            else:
                pfsum[b].append(pfsum[b][-1])
        pfsum[base][-1] += 1

    dp = [[None] * length for _ in range(length)] 

    def helper(i, j):
        # print(i, j)
        if i >= len(seq) or j >= len(seq) or i < 0 or j < 0:
            return 1
        if i > j:
            return 1
        if dp[i][j] is not None:
            return dp[i][j]
        length = j - i + 1
        if length % 2 != 0:
            dp[i][j] = 0
            return 0
        if length == 2:
            result = 1 if basePairing[seq[i]] == seq[j] else 0
            dp[i][j] = result
            return result
        A = pfsum["A"][j]
        G = pfsum["G"][j]
        C = pfsum["C"][j]
        U = pfsum["U"][j]
        if i != 0:
            A -= pfsum["A"][i - 1]
            G -= pfsum["G"][i - 1]
            C -= pfsum["C"][i - 1]
            U -= pfsum["U"][i - 1]
        if A != U or G != C:
            # print("base composition invalid")
            dp[i][j] = 0
            return 0
        ways = 0
        firstBase = seq[i]
        complement = basePairing[firstBase]
        for m in range(i + 1, j + 1):
            if seq[m] == complement:
                if m == i + 1:
                    ways += helper(m + 1, j)
                else:
                    ways += helper(i + 1, m - 1) * helper(m + 1, j)
        dp[i][j] = ways % 1000000
        return ways
    
    helper(0, length - 1)
    # print(dp)
    return dp[0][length - 1]

# slower
# def solution2(input):
#     s = "".join(input.splitlines()[1:])
#     c = {'':1, 'A':0, 'C':0, 'G':0, 'U':0, 'AA':0, 'AC':0, 'AG':0, 'AU':1, 'CA':0, 'CC':0, 
#     'CG':1, 'CU':0, 'GA':0, 'GC':1, 'GG':0, 'GU':0, 'UA':1, 'UC':0, 'UG':0, 'UU':0}

#     def catalan(s):
#         if s not in c:
#             c[s] = sum([catalan(s[1:k]) * c[s[0]+s[k]] * catalan(s[k+1:]) for k in range(1, len(s), 2)]) % 1000000
#         return c[s]

#     print(catalan(s))

# solution2('''>Rosalind_3285
# AGCGGCUAACGGCGCCGCGUGCCAUGGGCGCGUCGACUACGCCGCGCAUGCAUGUACUUA
# CGCGAUCGGAUUAGCCAUUUAAUUUAUGCAGCAUGGCCGCGCGCGCACUUGCAAAUCGGC
# GCGCCGGAAGCUCGCCGUAGAUUCGAGCGCCGUUAAAUAUUAAAUUGUAGUUAACCUGCU
# UUGCACUAUAGUACGGCGCUAAACCGGUAUAAACGCCGGCGCGCGGGCCUUGCAUGCAUA
# AGCGGCUAACGGCGCCGCGUGCCAUGGGCGCGUCGACUACGCCGCGCAUGCAUGUACUUA
# CGCGAUCGGAUUAGCCAUUUAAUUUAUGCAGCAUGGCCGCGCGCGCACUUGCAAAUCGGC
# GCGCCGGAAGCUCGCCGUAGAUUCGAGCGCCGUUAAAUAUUAAAUUGUAGUUAACCUGCU
# UUGCACUAUAGUACGGCGCUAAACCGGUAUAAACGCCGGCGCGCGGGCCUUGCAUGCAUA''')
print(solution('''>Rosalind_3285
AGCGGCUAACGGCGCCGCGUGCCAUGGGCGCGUCGACUACGCCGCGCAUGCAUGUACUUA
CGCGAUCGGAUUAGCCAUUUAAUUUAUGCAGCAUGGCCGCGCGCGCACUUGCAAAUCGGC
GCGCCGGAAGCUCGCCGUAGAUUCGAGCGCCGUUAAAUAUUAAAUUGUAGUUAACCUGCU
UUGCACUAUAGUACGGCGCUAAACCGGUAUAAACGCCGGCGCGCGGGCCUUGCAUGCAUA
AGCGGCUAACGGCGCCGCGUGCCAUGGGCGCGUCGACUACGCCGCGCAUGCAUGUACUUA
CGCGAUCGGAUUAGCCAUUUAAUUUAUGCAGCAUGGCCGCGCGCGCACUUGCAAAUCGGC
GCGCCGGAAGCUCGCCGUAGAUUCGAGCGCCGUUAAAUAUUAAAUUGUAGUUAACCUGCU
UUGCACUAUAGUACGGCGCUAAACCGGUAUAAACGCCGGCGCGCGGGCCUUGCAUGCAUA'''))




    

        
        
        
        
        
        
