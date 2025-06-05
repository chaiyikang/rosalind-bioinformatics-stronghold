from math import log10

def solution(seq: str, arr: str):
    arr = [float(val) for val in arr.split(" ")]
    result = []
    for gc in arr:
        gORc = gc / 2
        aORt = (1 - gc) / 2
        acc = 1
        for base in seq:
            if base == "G" or base == "C":
                acc *= gORc
            else:
                acc *= aORt
        result.append(log10(acc))
    print(*result)

solution('''TGGTCCAATGTACTATAGCATGCATTTCCAAGGCTCGTGGTGAATTACGAATATGCTCAAAGGGTGTGAAACCGTTTATAGGCTCAATATA''', '''0.089 0.150 0.193 0.235 0.281 0.368 0.380 0.454 0.476 0.529 0.599 0.681 0.731 0.748 0.830 0.884 0.902''')

