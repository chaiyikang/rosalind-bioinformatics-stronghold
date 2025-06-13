from math import comb, factorial

def solution(N, gc, seq):
    n = len(seq)

    at = 1 - gc


    acc = 1
    for base in seq:
        if base == "A" or base == "T":
            acc *= at / 2
        else:
            acc *= gc / 2
    print( 1 - ((1 - acc) ** N))

        # As = seq.count("A")
    # Gs = seq.count("G")
    # Ts = seq.count("T")
    # Cs = seq.count("C")

    # ATs = As + Ts
    # GCs = Gs + Cs
    # print(GCs / n)
    # if abs(GCs / n - gc) > 0.0001:
    #     return 0



    # acc = 1
    # for base in seq:
    #     if base == "A" or base == "T":
    #         acc *= (ATs / n) / 2
    #         ATs -= 1
    #     else:
    #         acc *= (GCs / n) / 2
    #         GCs -= 1
    # print( 1 - ((1 - acc) ** N))

solution(80293, 0.581242, "AAACGTATCG")





    
