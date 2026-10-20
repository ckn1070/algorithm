# Solved (매우 오래걸리고, 매우 간신히 풀었다)
# 으으.. 테두리에있는지 사각형 안에있는지 내가 어케알아;
# 그리고 그게 심지어 겹쳐있는지 어케아냐고;;
# 2배 해야됐던 것 같은데 그 이유는 뭐였지;;;
#
# 아 그냥 직사각형 전부 색칠해버릴까
# 어차피 50 이하 자연수이네
# 스케일업은 테두리 표현때문이 아니라, 오목한 부분에서 잘못 뛰어넘지 않도록 하기 위해서
# (3, 5) - (4, 5) - (5, 6) - (3, 6) 이걸 바로 (3, 5) - (3, 6) 해버리는걸 막기위해서 (둘 다 true니깐 가능하긴함)
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    maps = [[False] * 102 for _ in range(102)]

    for lx, ly, rx, ry in rectangle:
        for x in range(2 * lx, 2 * rx + 1):
            for y in range(2 * ly, 2 * ry + 1):
                maps[y][x] = True

    for lx, ly, rx, ry in rectangle:
        for x in range(2 * lx + 1, 2 * rx):
            for y in range(2 * ly + 1, 2 * ry):
                maps[y][x] = False

    print(maps[10])
    print(maps[9])
    print(maps[8])
    print(maps[7])
    print(maps[6])
    print(maps[5])
    print(maps[4])
    print(maps[3])
    print(maps[2])
    print(maps[1])

    q = deque([(characterX * 2, characterY * 2, 0)])
    visited = {(characterX * 2, characterY * 2)}
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        cur_x, cur_y, cnt = q.popleft()
        if cur_x == itemX * 2 and cur_y == itemY * 2:
            print('count', cnt)
            return cnt/2
        for _ in range(2):
            for i in range(4):
                x = dx[i]
                y = dy[i]
                nxt_x = cur_x + x
                nxt_y = cur_y + y
                if 0<=nxt_x<102 and 0<=nxt_y<102 and maps[nxt_y][nxt_x] and (nxt_x, nxt_y) not in visited:
                    print(cur_x, cur_y, cur_x+x, cur_y+y, cnt, maps[cur_y+y][cur_x+x])
                    q.append((cur_x+x, cur_y+y, cnt + 1))
                    visited.add((cur_x+x, cur_y+y))

    answer = 0
    return answer

solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8)
# solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1)
# solution([[1,1,5,7]], 1, 1, 4, 7)
# solution([[2,1,7,5],[6,4,10,10]], 3, 1, 7, 10)
# solution([[2,2,5,5],[1,3,6,4],[3,1,4,6]], 1, 4, 6, 3)