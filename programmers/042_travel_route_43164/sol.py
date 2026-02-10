# GPT (Hierholzer - 오일러 경로)
from collections import defaultdict

def solution(tickets):
    routes = defaultdict(list)
    for s, e in tickets:
        routes[s].append(e)

    # pop()으로 가장 작은 걸 꺼내려면 reverse 정렬
    for k in routes:
        routes[k].sort(reverse=True)

    stack = ["ICN"]
    path = []

    while stack:
        cur = stack[-1]
        if routes[cur]:
            stack.append(routes[cur].pop())
        else:
            path.append(stack.pop())

    return path[::-1]


# GPT 백트래킹
# from collections import defaultdict
#
# def solution(tickets):
#     routes = defaultdict(list)
#     for s, e in tickets:
#         routes[s].append(e)
#     for k in routes:
#         routes[k].sort()  # 오름차순
#
#     used = defaultdict(int)
#     for s, e in tickets:
#         used[(s, e)] += 1
#
#     n = len(tickets)
#     path = ["ICN"]
#
#     def dfs(cur):
#         if len(path) == n + 1:
#             return True  # 정답 완성
#
#         for nxt in routes[cur]:
#             if used[(cur, nxt)] == 0:
#                 continue
#             used[(cur, nxt)] -= 1
#             path.append(nxt)
#
#             if dfs(nxt):
#                 return True
#
#             path.pop()
#             used[(cur, nxt)] += 1
#
#         return False
#
#     dfs("ICN")
#     return path


# GPT Pop
# from collections import defaultdict
#
# def solution(tickets):
#     routes = defaultdict(list)
#     for s, e in tickets:
#         routes[s].append(e)
#     for k in routes:
#         routes[k].sort(reverse=True)
#
#     path = []
#     def dfs(cur):
#         while routes[cur]:
#             dfs(routes[cur].pop())
#         path.append(cur)  # 더 갈 데 없을 때 기록 (백트래킹 지점)
#
#     dfs("ICN")
#     return path[::-1]


# Programmers
# from collections import defaultdict
#
# def dfs(graph, N, key, footprint):
#     print(footprint)
#
#     if len(footprint) == N + 1:
#         return footprint
#
#     for idx, country in enumerate(graph[key]):
#         graph[key].pop(idx)
#
#         tmp = footprint[:]
#         tmp.append(country)
#
#         ret = dfs(graph, N, country, tmp)
#
#         graph[key].insert(idx, country)
#
#         if ret:
#             return ret
#
#
# def solution(tickets):
#     answer = []
#
#     graph = defaultdict(list)
#
#     N = len(tickets)
#     for ticket in tickets:
#         graph[ticket[0]].append(ticket[1])
#         graph[ticket[0]].sort()
#
#     answer = dfs(graph, N, "ICN", ["ICN"])
#
#     return answer