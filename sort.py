from collections import deque

def generate_reversals(perm):
    """Generate all possible reversals of a permutation."""
    reversals = []
    n = len(perm)
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            # Reverse the segment from index i to j-1 (inclusive)
            new_perm = perm[:i] + perm[i:j][::-1] + perm[j:]
            reversals.append((tuple(new_perm), (i + 1, j - 1 + 1)))
    
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
    # distance, permutation before, reversal applied
    forward_visited = {start: (0, None, None)}
    backward_visited = {target: (0, None, None)}
    
    level = 0
    
    while forward_queue or backward_queue:
        level += 1
        
        # Choose the smaller queue to expand (optimization)
        if len(forward_queue) <= len(backward_queue):
            # Forward search
            next_queue = deque()
            
            while forward_queue:
                current = forward_queue.popleft()
                current_dist = forward_visited[current][0]
                
                # Generate all possible reversals
                for next_perm, (i, j) in generate_reversals(list(current)):
                    # Check if we've met in the middle
                    if next_perm in backward_visited:
                        total_distance = current_dist + 1 + backward_visited[next_perm][0]
                        reversals = []
                        curr = current
                        # add forward path to reversals
                        while forward_visited[curr][2] is not None:
                            reversals.insert(0, forward_visited[curr][2])
                            curr = forward_visited[curr][1]

                        reversals.append(i, j)
                        # add backward path to reversals
                        curr = next_perm
                        while backward_visited[curr][2] is not None:
                            reversals.append(backward_visited[curr][2])
                            curr = backward_visited[curr][1]
                        
                        return total_distance, reversals
                    
                    # Add to forward search if not visited
                    if next_perm not in forward_visited:
                        forward_visited[next_perm] = (current_dist + 1, current, (i, j))
                        next_queue.append(next_perm)
            
            forward_queue = next_queue
        else:
            # Backward search
            next_queue = deque()
            
            while backward_queue:
                current = backward_queue.popleft()
                current_dist = backward_visited[current][0]
                
                # Generate all possible reversals
                for next_perm, (i, j) in generate_reversals(list(current)):
                    # Check if we've met in the middle
                    if next_perm in forward_visited:
                        total_distance = forward_visited[next_perm][0] + current_dist + 1

                        reversals = []
                        curr = current
                        # add backward path to reversals
                        while backward_visited[curr][2] is not None:
                            reversals.append(backward_visited[curr][2])
                            curr = backward_visited[curr][1]

                        reversals.insert(0, (i, j))
                        curr = next_perm
                        # add forward path to reversals
                        while forward_visited[curr][2] is not None:
                            reversals.insert(0, forward_visited[curr][2])
                            curr = forward_visited[curr][1]

                        return total_distance, reversals
                    
                    # Add to backward search if not visited
                    if next_perm not in backward_visited:
                        backward_visited[next_perm] = (current_dist + 1, current, (i, j))
                        next_queue.append(next_perm)
            
            backward_queue = next_queue
    
    return -1  # Should not reach here for valid permutations


def solution(input):
    s1, s2 = [[int(y) for y in x.split(" ")] for x in input.splitlines()]
    # print(bidirectional_bfs(s1, s2))
    result = bidirectional_bfs(s1, s2)
    print(result[0])
    for reversal in result[1]:
        print(*reversal)

solution('''2 1 10 5 3 7 9 4 8 6
4 10 3 2 5 7 8 9 6 1''')