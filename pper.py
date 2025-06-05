from math import factorial
def solution(n: int, k: int) -> int:
    return (factorial(n) / factorial(n - k)) % 1_000_000

print(solution(91, 9))