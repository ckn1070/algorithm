from collections import deque

# NOT Solved
# 시간 초과, 엣지케이스..
def solution(maps):

    arr = []
    visited = []
    def dfs(x, y, cnt):
        if x == len(maps[0]) - 1 and y == len(maps) - 1:
            arr.append(cnt)
            return

        if x < len(maps[0]) - 1 and maps[y][x + 1] == 1:
            dfs(x+1, y, cnt+1)
        if y < len(maps) - 1 and maps[y + 1][x] == 1:
            dfs(x, y+1, cnt+1)
        if y > 0 and maps[y - 1][x] == 1 and (x, y) not in visited:
            visited.append((x, y))
            dfs(x, y-1, cnt+1)

    dfs(0, 0, 1)

    if len(arr) > 0:
        arr.sort()
        answer = arr[0]
    else:
        answer = -1

    print(answer)
    return answer

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])


# def hor(total, i, j):
#     if total[i][j + 1] == 1:
#         return 1
#     else:
#         return 0
#
#
# def vet(total, i, j):
#     if total[i + 1][j] == 1:
#         return 1
#     else:
#         return 0
#
#
# x = 0
# y = 0
# cross = []
# visited = set()
#
# while x != len(maps[0]) - 1 and y != len(maps) - 1:
#     cur_x = hor(maps, x, y)
#     cur_y = vet(maps, x, y)
#     if cur_x == 1 and cur_y == 1:
#         cross.append((x, y))
#     elif cur_x == 1:

# cross = deque()
# x, y = 0, 0
# while x != len(maps[0]) - 1 and y != len(maps) - 1:
#     if x < len(maps[0]) - 1:
#         if maps[y][x + 1] == 1:
#             cross.append((x, y, 1))
#     if y < len(maps) - 1:
#         if maps[y + 1][x] == 1:
#             cross.append((x, y, 2))
#     if y > 0:
#         if maps[y - 1][x] == 1:
#             cross.append((x, y, 3))