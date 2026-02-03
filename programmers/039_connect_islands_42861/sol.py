# Programmers
def ancestor(node, parents):
    if parents[node] == node:
        return node
    else:
        return ancestor(parents[node], parents)

def solution(n, costs):
    answer = 0
    edges = sorted([(x[2], x[0], x[1]) for x in costs])
    parents = [i for i in range(n)]
    bridges = 0
    for w, f, t in edges:
        if ancestor(f, parents) != ancestor(t, parents):
            answer += w
            parents[ancestor(f, parents)] = t
            bridges += 1
        if bridges == n - 1:
            break
    return answer


# GPT
# Kruskal
# def solution(n, costs):
#     # Union-Find (Disjoint Set)
#     parent = list(range(n))
#     rank = [0] * n
#
#     def find(x):
#         while parent[x] != x:
#             parent[x] = parent[parent[x]]
#             x = parent[x]
#         return x
#
#     def union(a, b):
#         ra, rb = find(a), find(b)
#         if ra == rb:
#             return False
#         if rank[ra] < rank[rb]:
#             parent[ra] = rb
#         elif rank[ra] > rank[rb]:
#             parent[rb] = ra
#         else:
#             parent[rb] = ra
#             rank[ra] += 1
#         return True
#
#     # 1) 비용 기준 정렬
#     costs.sort(key=lambda x: x[2])
#
#     # 2) 싸이클 안 만들면 채택
#     answer = 0
#     edges = 0
#     for a, b, c in costs:
#         if union(a, b):
#             answer += c
#             edges += 1
#             if edges == n - 1:
#                 break
#
#     return answer


# GPT
# Prim
# import heapq
# from collections import defaultdict
#
# def solution(n, costs):
#     graph = defaultdict(list)
#     for a, b, c in costs:
#         graph[a].append((c, b))
#         graph[b].append((c, a))
#
#     visited = [False] * n
#     pq = [(0, 0)]  # (cost, node)
#     total = 0
#     taken = 0
#
#     while pq and taken < n:
#         cost, node = heapq.heappop(pq)
#         if visited[node]:
#             continue
#         visited[node] = True
#         total += cost
#         taken += 1
#
#         for nxt_cost, nxt in graph[node]:
#             if not visited[nxt]:
#                 heapq.heappush(pq, (nxt_cost, nxt))
#
#     return total
