from collections import deque

# GPT
def solution(maps):
    n = len(maps)        # 세로(y)
    m = len(maps[0])     # 가로(x)

    # 시작/도착이 막혀 있으면 즉시 불가
    if maps[0][0] == 0 or maps[n-1][m-1] == 0:
        return -1

    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((0, 0, 1))  # x, y, 거리
    visited[0][0] = True

    # 상하좌우
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    while q:
        x, y, dist = q.popleft()

        if x == m - 1 and y == n - 1:
            return dist

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and maps[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append((nx, ny, dist + 1))

    return -1

# Programmers
# from collections import deque
#
# def solution(maps):
#     x_move = [1, 0, -1, 0]
#     y_move = [0, 1, 0, -1]
#
#     x_h, y_h = (len(maps[0]), len(maps))
#     queue = deque([(0, 0, 1)])
#
#     while queue:
#         x, y, d = queue.popleft()
#
#         for i in range(4):
#             nx = x + x_move[i]
#             ny = y + y_move[i]
#
#             if nx > -1 and ny > -1 and nx < x_h and ny < y_h:
#                 if maps[ny][nx] == 1 or maps[ny][nx] > d + 1:
#                     maps[ny][nx] = d + 1
#                     if nx == x_h - 1 and ny == y_h - 1:
#                         return d + 1
#
#                     queue.append((nx, ny, d + 1))
