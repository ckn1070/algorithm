# Half Solved
def solution(n, computers):

    def rec(ith, route):
        for i, v in enumerate(computers[ith]):
            if i <= ith:
                continue
            if v == 1:
                route.append(i)
                rec(i, route)
        return route

    answer = 0
    cur = set()
    for j in range(len(computers)):
        if j not in cur:
            cur.update(rec(j, [j]))
            answer += 1
        if len(cur) == len(computers):
            break

    print(answer)
    return answer

solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]])