# Solved
# 18/21, 2/4 -> 정답 (-1, 0) 이런거 빼면 안된다
# 거리까지 Q에 넣는것까지도 맞다
from collections import deque

def solution(maps):
    m = len(maps) # height
    n = len(maps[0]) # width
    visited = [[False] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if maps[i][j] == 0:
                visited[i][j] = True

    visited[0][0] = True
    q = deque([(0, 0, 1)])
    answer = -1
    while q:
        (curx, cury, mv) = q.popleft()
        answer += 1
        print('cur', curx, cury, mv)
        for dx, dy in [(1, 0), (0, 1), (0, -1)]:
            x = curx + dx
            y = cury + dy
            if 0<=y<m and 0<=x<n and not visited[y][x]:
                print('nxt', x, y)
                if not (x == n-1 and y == m-1):
                    visited[y][x] = True
                    q.append((x, y, mv+1))
                else:
                    print('correct', x, y, mv+1)
                    return mv+1

    if not visited[m-1][n-1]:
        answer = -1

    print(visited, answer)
    return answer

solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])