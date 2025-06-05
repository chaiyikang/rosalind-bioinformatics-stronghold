import math

def solution(input: str) -> int:
    seq = "".join(input.splitlines()[1:])
    As = 0
    Gs = 0
    for base in seq:
        if base == "A":
            As += 1
        elif base == "G":
            Gs += 1
    return math.factorial(As) * math.factorial(Gs)

print(solution('''>Rosalind_5257
UUAGGUAGUAUUAAUGGAACCUUCGGAUAUCCAGGUGAUAACGAGUCGUCCGCCUCCGCA
AAACUGUGGACAUCCCGUCG'''))
