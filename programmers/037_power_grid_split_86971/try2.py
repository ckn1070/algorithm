# Solved
# 이거 굉장히 고난의 문제였던 것 같은데..
# n이 100이하
# wire는 n-1
#
# wire 하나씩 끊어보면 되겠네?
#
# 이걸 왜이렇게 어렵게 풀었지..?
# 그래프 탐색하는거에서 완전 꽉막혔네;
from collections import defaultdict, deque

def can_go(n, x, y, d):
    visited = [False] * n
    visited[x] = True
    visited[y] = True
    q = deque([x])

    cnt = 1
    while q:
        cur = q.popleft()
        for nxt in d[cur]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
                cnt += 1

    return cnt

def solution(n, wires):
    d = defaultdict(list)
    for a, b, in wires:
        d[a].append(b)
        d[b].append(a)

    answer = 10**18
    for x, y in wires:
        left = can_go(n+1, x, y, d)
        right = can_go(n+1, y, x, d)
        answer = min(abs(left-right), answer)

    print(answer)
    return answer

solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])
solution(4, [[1,2],[2,3],[3,4]])
solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]])