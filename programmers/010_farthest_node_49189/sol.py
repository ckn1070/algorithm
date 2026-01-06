from collections import deque

# GPT
def solution(n, edge):
    # 1) 인접 리스트 만들기 (무방향 그래프)
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    print('graph: ', graph)

    # 2) 최단거리 배열 (0이면 미방문, 1번은 거리 0)
    dist = [-1] * (n + 1)
    dist[1] = 0

    # 3) BFS
    q = deque([1])
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                q.append(nxt)

    # 4) 가장 먼 거리의 노드 개수
    max_dist = max(dist[1:])          # 0번 인덱스 제외
    return dist.count(max_dist)

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