# NOT Solved
# 3/10 맞았는데, 나머지는 시간초과 (그럴 줄 알았다) - 지나치게 복잡하게 풀었다
#
# 각 노드별로 최단거리 하나씩만 남겨두면 되잖아
# DFS로 계산하면 처음 계산되는 거리가 곧 최단거리가 되지
#
# Try 2
from collections import deque as dq

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    for a, b, in edge:
        graph[a].append(b)
        graph[b].append(a)

    dist = [-1] * (n + 1)
    dist[1] = 0

    q = dq([1])
    while q:
        cur = q.popleft()
        for node in graph[cur]:
            if dist[node] == -1:
                dist[node] = dist[cur] + 1
                q.append(node)

    far = max(dist[1:])
    answer = dist.count(far)
    print('answer', answer)
    return answer


# Try 1
# from collections import defaultdict as dd, deque as dq
#
# def solution(n, edge):
#     graph = dd(list)
#     for a, b in edge:
#         graph[a].append(b)
#         graph[b].append(a)
#
#     q = dq([[1]])
#     dist = dd(int)
#     for m in range(1, n + 1):
#         dist[m] = 0 if m == 1 else n
#     while q:
#         cur = q.popleft()
#         nxt = graph[cur[-1]]
#         for i in nxt:
#             if i not in cur:
#                 route = cur[:]
#                 route.append(i)
#                 q.append(route)
#             else:
#                 if dist[cur[-1]] > len(cur):
#                     dist[cur[-1]] = len(cur)
#
#     print('dist', dist)
#
#     answer = 0
#     maximum = 0
#     for k in dist.keys():
#         if dist[k] > maximum:
#             maximum = dist[k]
#     for l in dist.keys():
#         if dist[l] == maximum:
#             answer += 1
#
#     print('answer', answer)
#     return answer

solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])


# Programmers
# def solution(n, edge):
#     graph =[  [] for _ in range(n + 1) ]
#     distances = [ 0 for _ in range(n) ]
#     is_visit = [False for _ in range(n)]
#     queue = [0]
#     is_visit[0] = True
#     for (a, b) in edge:
#         graph[a-1].append(b-1)
#         graph[b-1].append(a-1)
#
#     while queue:
#         i = queue.pop(0)
#
#         for j in graph[i]:
#             if is_visit[j] == False:
#                 is_visit[j] = True
#                 queue.append(j)
#                 distances[j] = distances[i] + 1
#
#     distances.sort(reverse=True)
#     answer = distances.count(distances[0])
#
#     return answer