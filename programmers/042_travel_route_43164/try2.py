# Solved
# BFS 할랬는데 DFS 해야할것같은데
# 항공권을 모두 사용해야하는게 킥이네
#
# 오일러 경로가 있네..?
from collections import defaultdict, deque
# Try 2
def solution(tickets):
    routes = defaultdict(list)
    for s, e in tickets:
        routes[s].append(e)
    n = len(tickets)

    answer = []
    def dfs(cur, visited, left):
        if len(visited) == n + 1:
            print('oh', visited)
            answer.append(visited[:])
            return

        for nxt in routes[cur]:
            if [cur, nxt] in left:
                visited.append(nxt)
                left.remove([cur, nxt])
                print('nxt', nxt, visited, n)
                dfs(nxt, visited, left)
                print('end', visited)
                left.append([cur, nxt])
                visited.pop()

    dfs("ICN", ["ICN"], tickets)
    answer.sort()
    print(answer)

    return answer[0]


# Try 1
# def solution(tickets):
#     routes = defaultdict(list)
#     for s, e in tickets:
#         routes[s].append(e)
#     n = len(tickets)
#
#     q = deque([("ICN", ["ICN"])])
#     answer = []
#     while q:
#         cur, acc = q.popleft()
#         for nxt in routes[cur]:
#             print('cur', cur, nxt, acc)
#             acc.append(nxt)
#             if len(acc) <= n + 1:
#                 q.append((nxt, acc))
#         if not q:
#             answer.append(acc)
#
#     print('answer', answer)
#     return answer

solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])