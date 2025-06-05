import sys



def permutations(lst):
    if len(lst) == 1:
        return [[lst[0]], [-lst[0]]]
    return [
    [x * sign] + perm
    for sign in [1, -1]
    for x in lst
    for perm in permutations([y for y in lst if y != x])
    ]

def solution(n):
    lst = [i for i in range(1, n+ 1)]
    res = permutations(lst)
    print(len(res))
    for perm in res:
        print(*perm, file=f)

with open('output.txt', 'w') as f:
    solution(4)
