# GPT
def solution(n, computers):
    visited = set()

    def rec(ith):
        visited.add(ith)
        for i, v in enumerate(computers[ith]):
            if v == 1 and i not in visited:
                rec(i)

    answer = 0
    for j in range(n):
        if j not in visited:
            rec(j)
            answer += 1
    return answer

# def solution(n, computers):
#     visited = set()
#     answer = 0
#
#     def dfs(start):
#         stack = [start]
#         visited.add(start)
#         while stack:
#             node = stack.pop()
#             for nxt, v in enumerate(computers[node]):
#                 if v == 1 and nxt not in visited:
#                     visited.add(nxt)
#                     stack.append(nxt)
#
#     for i in range(n):
#         if i not in visited:
#             dfs(i)
#             answer += 1
#
#     return answer

# Programmers
# def solution(n, computers):
#     answer = 0
#     visited = [0 for i in range(n)]
#     def dfs(computers, visited, start):
#         stack = [start]
#         while stack:
#             j = stack.pop()
#             if visited[j] == 0:
#                 visited[j] = 1
#             # for i in range(len(computers)-1, -1, -1):
#             for i in range(0, len(computers)):
#                 if computers[j][i] ==1 and visited[i] == 0:
#                     stack.append(i)
#     i=0
#     while 0 in visited:
#         if visited[i] ==0:
#             dfs(computers, visited, i)
#             answer +=1
#         i+=1
#     return answer