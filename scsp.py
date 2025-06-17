import helpers

def longestCommonSubsequence(text1: str, text2: str) -> int:
        length1 = len(text1)
        length2 = len(text2)
        dp = [[0] * (length2 + 1) for _ in range(length1 + 1)]
        parent = [[None] * (length2 + 1) for _ in range(length1 + 1)]
        for i in range(1, length1 + 1):
            for  j in range(1, length2 + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    # parent[i][j] = (text1[i - 1], (i - 1, j - 1))
                    parent[i][j] = ((i - 1, j - 1), (i - 1, j - 1))
                else:
                    if dp[i - 1][j] > dp[i][j - 1]:
                        dp[i][j] = dp[i - 1][j]
                        parent[i][j] = ("", (i - 1, j))
                    else:
                        dp[i][j] = dp[i][j - 1]
                        parent[i][j] = ("", (i, j - 1))
        curr = parent[length1][length2]
        # result = ""
        indices1 = []
        indices2 = []
        while curr is not None:
            if curr[0]:
                 indices1.insert(0, curr[0][0])
                 indices2.insert(0, curr[0][1])
            curr = parent[curr[1][0]][curr[1][1]]
        return indices1, indices2

        return dp[length1][length2]

def solution(input):
    s1, s2 = input.splitlines()
    s1, s2 = list(s1), list(s2)

    indices1, indices2 = longestCommonSubsequence(s1, s2)
    print(indices1, indices2)
    offset = 0
    # use s2 as the template. we want to add chars of s1 that are not in the LCS into s2, into the correct positions
    # chars inbetween two characters in the LCS in s1 must also end up inbetween the corresponding matched LCS characters in s2
    # to simplify logic, for each LCS character, copy the non-LCS characters before it (and after previous LCS character) into the left of the LCS character in s2
    # at the end we must remember to add everything after the last LCS character, to the right in s2, because our loop didnt capture it
    for i in range(len(indices1)):
        r1 = indices1[i]
        r2 = indices2[i]
        if i == 0:
            package =  s1[0:r1]
            s2[r2:r2] = package
            offset += len(package)
        else:
            package = s1[indices1[i - 1] + 1:r1]
            s2[r2 + offset:r2 + offset] = package
            offset += len(package)

        # append substring after last matching to result
        lastPackage = s1[indices1[-1] + 1:]
        s2[len(s2):] = lastPackage
    print("".join(s2))


          



solution('''AGTCGAACGTGCTACGAAAGAAGTTGCTGCCAAGGCAAAGTGTGACAGATGGGCATCGCCGGACTGACGCAGAGTATACTAGTTGA
ATAGGGTCCGTGTTCCACATTCGCGGCGCGTTGCTTCTCTTCCATTGGTAGCGTCGGAGATACAAGTTGAACGCTATTAGGCAGGTTCAGA''')