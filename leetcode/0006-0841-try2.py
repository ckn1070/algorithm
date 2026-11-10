# Solved
class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        visited[0] = True

        def dfs(room):
            for k in rooms[room]:
                if not visited[k]:
                    visited[k] = True
                    dfs(k)

        dfs(0)
        return visited.count(False) == 0