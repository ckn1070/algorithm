# NOT Solved
# 완전 감을 잘못 잡음
from collections import defaultdict as dd, deque

def solution(n, costs):
    imap = dd(list)
    q = deque([(0, 0)])
    visited = set()

    for i, j, c in costs:
        imap[i].append((j, c))
        imap[j].append((i, c))
    for k in imap.keys():
        imap[k].sort(reverse=True)

    def dfs(cur):
        candidate = imap[cur]
        nxt = candidate[0]
        print(cur, candidate)
        for l in range(len(candidate)-1, -1, -1):
            if candidate[l][0] not in visited:
                nxt = candidate[l]
                break
        imap[cur].pop()
        print('nxt', nxt)
        return nxt

    while q:
        step = q.popleft()
        visited.add(step)
        if len(visited) < n:
            tmp = dfs(step[0])
            q.append(tmp)
        else:
            break

    answer = 0
    print(visited)
    for _, n in visited:
        answer += n
    print(answer)

    return answer

solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])