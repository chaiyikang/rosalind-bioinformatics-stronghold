def clean(alphabet, n):
    return alphabet if n == 1 else [
            c + perm
            for c in alphabet
            for perm in clean(alphabet, n - 1)
            ]

    
result = clean("A B C D E F".split(" "), 3)
for s in result:
    print(s)

