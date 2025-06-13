from math import comb, factorial

def solution(input):
    sequence = "".join(input.splitlines()[1:])
    print(sequence)
    As = 0
    Us = 0
    Gs = 0
    Cs = 0
    for base in sequence:
        if base == "A":
            As += 1
        elif base == "U":
            Us += 1
        elif base == "G":
            Gs += 1
        else:
            Cs += 1
    print(As, Us, Gs, Cs)
    return comb(max(As, Us), min(As, Us)) * factorial(min(As, Us)) * comb(max(Gs, Cs), min(Gs, Cs)) * factorial(min(Gs, Cs))

print(solution('''>Rosalind_5020
GAGGUACAUUAUACAAAGCAAUCUCAAUUUUCCAACUCGGCAAGCACCGUUCCACAAGGC
AUUGCGACGUCACCUGUAGGAUGAAGGAUUUA'''))