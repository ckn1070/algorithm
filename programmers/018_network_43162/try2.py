# NOT Solved
#
# 일단 컴퓨터를 처음부터 끝까지 한 번만 훑으면 된다 - for n
# 각 컴퓨터에 대해서 갈 수 있는 끝까지 가보고 - DFS
# 남은 것들은 횟수를 올려서 다음으로
#
# DFS로 들어가면 될 것 같은데
def solution(n, computers):
    visited = set()

    def rec(com):
        visited.add(com)
        for idx, j in enumerate(computers[com]):
            if idx != com and j == 1 and idx not in visited:
                rec(idx)

    answer = 0
    for i in range(n):
        if i not in visited:
            rec(i)
            print('i', i, visited)
            answer += 1

    print(answer)
    return answer


# Try 1
# from collections import defaultdict as dd
#
# def solution(n, computers):
#     graph = dd(list)
#
#     for i, computer in enumerate(computers):
#         for j, connection in enumerate(computer):
#             if i != j and connection == 1:
#                 if j not in graph[i]:
#                     graph[i].append(j)
#                 if i not in graph[j]:
#                     graph[j].append(i)
#     print(graph)
#
#     visited = set()
#     visited.add(0)
#
#     while len(visited) != n:
#         for i in visited:
#             nxt = graph[i]
#             for j in nxt:
#                 visited.add(j)
#                 print(i, j, visited)
#
#     answer = 0
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

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])