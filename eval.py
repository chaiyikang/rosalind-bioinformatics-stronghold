def solution(n, seq, arr):
    arr = arr.split(" ")
    result = []
    substrings = n - len(seq) + 1
    for gc in arr:
        p = 1
        for base in seq:
            if base == "G" or base == "C":
                p *= float(gc) / 2
            else:
                p *= (1 - float(gc)) / 2
        result.append(round(substrings * p, 3))
    print(*result)

solution(943186,
"TATGTAAT",
"0.000 0.101 0.107 0.197 0.243 0.290 0.352 0.377 0.449 0.489 0.550 0.588 0.672 0.716 0.777 0.813 0.875 0.929 1.000")
