# Solved
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """

        def dfs(k, v):
            for key in k:
                if not v[key]:
                    v[key] = True
                    dfs(rooms[key], v)

        visited = [False] * len(rooms)
        visited[0] = True
        dfs(rooms[0], visited)
        print(visited)
        return visited.count(False) == 0


# GPT
# class Solution:
#     def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
#         n = len(rooms)
#         visited = [False] * n
#         visited[0] = True
#
#         stack = [0]
#
#         while stack:
#             cur = stack.pop()
#
#             for key in rooms[cur]:
#                 if not visited[key]:
#                     visited[key] = True
#                     stack.append(key)
#
#         return all(visited)