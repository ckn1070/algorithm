from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    map = [[0] * 51 for _ in range(51)]
    print(len(map))
    q = deque()

    for x1, y1, x2, y2 in rectangle:
        if ((characterX == x1 or characterX == x2)
                and (characterY == y1 or characterY == y2)):
            q.append([x1, y1, x2, y2])

    print(q)
    answer = 0
    return answer

solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8)
solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1)
solution([[1,1,5,7]], 1, 1, 4, 7)
solution([[2,1,7,5],[6,4,10,10]], 3, 1, 7, 10)
solution([[2,2,5,5],[1,3,6,4],[3,1,4,6]], 1, 4, 6, 3)