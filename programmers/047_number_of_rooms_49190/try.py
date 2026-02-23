def solution(arrows):
    route = {0: (0, 1), 1: (1, 1), 2: (1, 0), 3: (1, -1), 4: (0, -1), 5: (-1, -1), 6: (-1, 0), 7: (-1, 1)}
    cur = (0, 0)
    visited = [(0, 0)]

    answer = 0
    for i in arrows:
        x, y = route[i]
        a, b = cur
        cur = (x+a, y+b)
        if cur in visited:
            answer+=1
        visited.append(cur)

    print(visited)
    print(answer)
    return answer

solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0])