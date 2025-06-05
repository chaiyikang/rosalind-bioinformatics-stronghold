def permutations(arr):
    if len(arr) == 1:
        return [[arr[0]]]
    return [
        [x] + perm
        for x in arr
        for perm in permutations([y for y in arr if y != x])
    ]


# arr.map(x =>
#         permutations(arr.filter(y => y != x)).map(perm =>
#                                                   [x] + perm))

def solution(n :int):
    arr = [i + 1 for i in range(n)]
    result = permutations(arr)
    print(len(result))
    for permutation in result:
        print(*permutation)

# solution(6)

from itertools import permutations
list_of_permutations = list(permutations(range(1,5+1)))
print(list_of_permutations)
