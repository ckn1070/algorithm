# Solved - 한 번에..?
#
# 문제를 보면 DFS를 해야겠다는 생각이 드네
# 하나에서 쭉 파고들면서 어디까지 연결됐는지 확인하기
#
# Union Find 가능
from typing import List
from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        connections = defaultdict(set)
        visited = [False] * n

        for i in range(n):
            for j in range(n):
                if isConnected[j][i] == 1:
                    connections[i].add(j)
                    connections[j].add(i)

        def dfs(cur):
            for nxt in connections[cur]:
                if not visited[nxt]:
                    visited[nxt] = True
                    dfs(nxt)

        answer = 0
        for k in range(n):
            if not visited[k]:
                dfs(k)
                answer += 1

        return answer


# GPT
# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         n = len(isConnected)
#         visited = [False] * n
#
#         def dfs(cur):
#             visited[cur] = True
#
#             for nxt in range(n):
#                 if isConnected[cur][nxt] == 1 and not visited[nxt]:
#                     dfs(nxt)
#
#         answer = 0
#
#         for i in range(n):
#             if not visited[i]:
#                 answer += 1
#                 dfs(i)
#
#         return answer

# GPT - Union Find
# class Solution:
#     def findCircleNum(self, isConnected: List[List[int]]) -> int:
#         n = len(isConnected)
#         parent = list(range(n))
#         size = [1] * n
#         answer = n
#
#         def find(x):
#             while parent[x] != x:
#                 parent[x] = parent[parent[x]]
#                 x = parent[x]
#             return x
#
#         def union(a, b):
#             ra, rb = find(a), find(b)
#
#             if ra == rb:
#                 return False
#
#             if size[ra] < size[rb]:
#                 ra, rb = rb, ra
#
#             parent[rb] = ra
#             size[ra] += size[rb]
#             return True
#
#         for i in range(n):
#             for j in range(i + 1, n):
#                 if isConnected[i][j] == 1:
#                     if union(i, j):
#                         answer -= 1
#
#         return answer