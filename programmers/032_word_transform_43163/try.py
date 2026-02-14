# Solved
from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    def nxt(before, after):
        n, cnt = len(before), 0
        for i in range(n):
            if before[i] == after[i]:
                cnt +=1
        return cnt == n-1

    q = deque([(begin, 0)])
    visited = []
    while q:
        cur, d = q.popleft()
        for i in words:
            if i not in visited and nxt(cur, i):
                if i == target:
                    return  d+1
                q.append((i, d+1))
                visited.append(i)


    answer = 0
    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))