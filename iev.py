def solution(couples):
    q, w, e, r, t, y = couples
    return (q + w + e + r * 0.75 + t * 0.5) * 2
print(solution([16783, 19661, 17719, 16365, 18719, 16708]))