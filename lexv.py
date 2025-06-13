def solution(alphabet, n):
    if n == 1:
        return alphabet
    result = []
    for alpha in alphabet:
        result.append(alpha)
        for prev in solution(alphabet, n - 1):
            result.append(alpha + prev)
    return result

print(*solution("O K B E S Z R A Q M H U".split(" "), 3))
            
