# GPT
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    MAX = 102  # 50*2 + 여유
    board = [[0]*MAX for _ in range(MAX)]

    # 1) 스케일업해서 일단 전부 1로 칠하기
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                board[x][y] = 1

    # 2) 내부를 0으로 지우기 (테두리만 남김)
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1*2, y1*2, x2*2, y2*2
        for x in range(x1+1, x2):
            for y in range(y1+1, y2):
                board[x][y] = 0

    # 3) BFS는 테두리(1)만 이동
    sx, sy = characterX*2, characterY*2
    tx, ty = itemX*2, itemY*2

    q = deque([(sx, sy, 0)])
    visited = [[False]*MAX for _ in range(MAX)]
    visited[sx][sy] = True

    dirs = [(1,0), (-1,0), (0,1), (0,-1)]

    while q:
        x, y, d = q.popleft()
        if x == tx and y == ty:
            return d // 2  # 스케일업 보정

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < MAX and 0 <= ny < MAX:
                if not visited[nx][ny] and board[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny, d+1))

    return 0


# Programmers
# import itertools
#
#
# def is_movable(cur_x, cur_y, next_x, next_y, rectangles):
#     x, y = (cur_x + next_x) / 2, (cur_y + next_y) / 2
#     is_on_any_border = any(
#         (x in (x1, x2) and y1 <= y <= y2) or (y in (y1, y2) and x1 <= x <= x2)
#         for x1, y1, x2, y2 in rectangles)
#     is_inside_any_rect = any(
#         x1 < x < x2 and y1 < y < y2 for x1, y1, x2, y2 in rectangles)
#     return is_on_any_border and not is_inside_any_rect
#
#
# def solution(rectangle, characterX, characterY, itemX, itemY):
#     cur_pos = (characterX, characterY)
#     prev_pos = None
#     for dist in itertools.count():
#         if cur_pos == (characterX, characterY) and prev_pos:
#             perimeter = dist
#             break
#         elif cur_pos == (itemX, itemY):
#             dist_to_item = dist
#         for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
#             next_pos = (cur_pos[0] + dx, cur_pos[1] + dy)
#             if next_pos != prev_pos and is_movable(*cur_pos, *next_pos,
#                                                    rectangle):
#                 prev_pos, cur_pos = cur_pos, next_pos
#                 break
#     return min(dist_to_item, perimeter - dist_to_item)