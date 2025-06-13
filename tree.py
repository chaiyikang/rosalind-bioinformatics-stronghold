# Replace 'filename.txt' with the path to your file
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Strip newline characters if you want clean strings
lines = [line.strip() for line in lines]

def solution(arr):
    n = int(arr[0])
    e = len(arr) - 1
    return n - 1 - e

print(solution(lines))