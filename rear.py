# from collections import deque

# def invert(s1, i, j):
#         s = list(s1)
#         s[i:j + 1] = s[i:j + 1][::-1]
#         return s

# def findDistance(s1, s2):
#     if s1 == s2:
#         return 0
#     queue = deque()
#     queue.append([s2, 0])
#     added = set()
#     added.add(tuple(s2))
#     # print(added)
#     while queue:
#         ss2, inversions = queue.popleft()
#         # print(ss2)
#         # print(s1, ss2)
#         if s1 == ss2:
#             return inversions
#         # print(inversions)
#         for i in range(len(s1)):
#             for j in range(i, len(s1)):
#                 new = invert(ss2, i, j)
#                 # print(new)
#                 if tuple(new) not in added:
#                     queue.append([new, inversions + 1])
#                     added.add(tuple(new))
#     # print("fuck")


     
    


# def solution(input):
#     seq = [
#         [int(x) for x in line.split(" ")]
#         for line in input.splitlines()
#         if line.strip() != ""
#     ]
#     # print(seq)

#     result = []
#     for i in range(0, len(seq), 2):
#     # for i in range(0, 2, 2):
#         s1 = seq[i]
#         s2 = seq[i + 1]
#         result.append(findDistance(s1, s2))
#     print(*result)






# print(solution('''8 6 7 9 4 1 3 10 2 5
# 8 2 7 6 9 1 5 3 10 4'''))

from collections import deque

def generate_reversals(perm):
    """Generate all possible reversals of a permutation."""
    reversals = []
    n = len(perm)
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            # Reverse the segment from index i to j-1 (inclusive)
            new_perm = perm[:i] + perm[i:j][::-1] + perm[j:]
            reversals.append(tuple(new_perm))
    
    return reversals

def bidirectional_bfs(start, target):
    """
    Find the minimum number of reversals to transform start to target
    using bidirectional BFS.
    """
    if start == target:
        return 0
    
    # Convert to tuples for hashing
    start = tuple(start)
    target = tuple(target)
    
    # Queues for forward and backward search
    forward_queue = deque([start])
    backward_queue = deque([target])
    
    # Visited sets with distances
    forward_visited = {start: 0}
    backward_visited = {target: 0}
    
    level = 0
    
    while forward_queue or backward_queue:
        level += 1
        
        # Choose the smaller queue to expand (optimization)
        if len(forward_queue) <= len(backward_queue):
            # Forward search
            next_queue = deque()
            
            while forward_queue:
                current = forward_queue.popleft()
                current_dist = forward_visited[current]
                
                # Generate all possible reversals
                for next_perm in generate_reversals(list(current)):
                    # Check if we've met in the middle
                    if next_perm in backward_visited:
                        return current_dist + 1 + backward_visited[next_perm]
                    
                    # Add to forward search if not visited
                    if next_perm not in forward_visited:
                        forward_visited[next_perm] = current_dist + 1
                        next_queue.append(next_perm)
            
            forward_queue = next_queue
        else:
            # Backward search
            next_queue = deque()
            
            while backward_queue:
                current = backward_queue.popleft()
                current_dist = backward_visited[current]
                
                # Generate all possible reversals
                for next_perm in generate_reversals(list(current)):
                    # Check if we've met in the middle
                    if next_perm in forward_visited:
                        return forward_visited[next_perm] + current_dist + 1
                    
                    # Add to backward search if not visited
                    if next_perm not in backward_visited:
                        backward_visited[next_perm] = current_dist + 1
                        next_queue.append(next_perm)
            
            backward_queue = next_queue
    
    return -1  # Should not reach here for valid permutations

def solve_reversal_distances(input_text):
    """
    Solve the reversal distance problem for multiple permutation pairs.
    """
    lines = [x for x in input_text.strip().split('\n') if x != '']
    print(lines)
    results = []
    
    i = 0
    while i < len(lines):
        if i + 1 < len(lines):
            # Parse two consecutive lines as a pair
            perm1 = list(map(int, lines[i].split()))
            perm2 = list(map(int, lines[i + 1].split()))
            
            # Calculate reversal distance
            distance = bidirectional_bfs(perm1, perm2)
            results.append(distance)
            
            i += 2
        else:
            break
    
    return results

# Test with the sample dataset
sample_input = """9 5 7 8 1 3 4 2 6 10
10 7 4 1 8 5 9 3 2 6

2 7 6 5 1 10 4 9 3 8
6 4 1 9 7 8 3 5 10 2

3 7 9 4 1 5 10 2 8 6
9 7 4 10 1 8 3 2 6 5

10 4 3 7 6 5 2 9 1 8
3 10 6 4 2 7 1 5 8 9

6 3 1 9 2 5 4 7 10 8
1 8 5 6 4 7 10 3 2 9"""

if __name__ == "__main__":
    results = solve_reversal_distances(sample_input)
    print("Reversal distances:", " ".join(map(str, results)))
    
    # Test individual pair for debugging
    # print("\nTesting individual cases:")
    # test_cases = [
    #     ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [3, 1, 5, 2, 7, 4, 9, 6, 10, 8]),
    #     ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    # ]
    
    # for i, (perm1, perm2) in enumerate(test_cases):
    #     dist = bidirectional_bfs(perm1, perm2)
    #     print(f"Case {i+1}: Distance = {dist}")