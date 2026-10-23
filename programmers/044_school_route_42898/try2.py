# Solved
# ? 이걸 풀었다고?
def solution(m, n, puddles):
    route = [[0] * m for _ in range(n)]

    route[0][0] = 1
    for a, b in puddles:
        route[b - 1][a - 1] = -1
    print(route)

    for x in range(m):
        for y in range(n):
            if y > 0: up = route[y - 1][x]
            else: up = 0

            if x > 0: left = route[y][x - 1]
            else: left = 0

            print('up', up, 'left', left, x, y)
            if route[y][x] != -1:
                if up != -1: route[y][x] += up
                if left != -1: route[y][x] += left
            print(route)

    answer = route[n-1][m-1] % 1_000_000_007
    print('answer', answer)
    return answer

# solution(4, 3, [[2, 2]])
solution(4, 3, [[3, 2]])