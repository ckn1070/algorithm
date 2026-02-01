# Solved
from collections import defaultdict as dd, deque

def solution(n, wires):
    tree = dd(list)

    for v1, v2 in wires:
        tree[v1].append(v2)
        tree[v2].append(v1)
    # print(tree)

    def rec(start, broken):
        visited = set()
        visited.add(start)
        q = deque()
        for i in tree[start]:
            if i != broken:
                q.append(i)

        while q:
            # print(start, broken, visited, q)
            cur = q.popleft()
            if cur not in visited:
                visited.add(cur)
                q.extend(tree[cur])

        # print(start, broken, visited)
        return len(visited)

    answer = 100
    for x, y in wires:
        left = rec(x, y)
        right = rec(y, x)
#         print(n, left, right)
        answer = min(answer, abs(left - right))
        print(answer)


    return answer

solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]])
solution(4, [[1,2],[2,3],[3,4]])
solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]])