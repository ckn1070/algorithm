# Solved
from collections import defaultdict

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        con = defaultdict(set)

        for i in range(n):
            for j in range(i, n):
                if isConnected[i][j] == 1:
                    con[i].add(j)
                    con[j].add(i)

        def dfs(cur):
            for nxt in con[cur]:
                if not visited[nxt]:
                    visited[nxt] = True
                    dfs(nxt)

        prov = 0
        for k in range(n):
            if not visited[k]:
                dfs(k)
                prov += 1

        return prov
