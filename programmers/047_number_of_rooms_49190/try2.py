# NOT Solved
#
# 여기선 단순히 Node가 아니라 Edge를 관리해야 할 것 같은데..
#
# 현재 상태에서 바로 계산하면 교차점이 소숫점에서 생길 수 있음 -> 2배로 스케일 확대 필요
# 말 그대로 노드와 엣지만 잘 계산하면 된다
# 노드가 있던 것인지, 엣지가 있던 것인지
def solution(arrows):
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    v_node = set()
    v_edge = set()
    v_node.add((0,0))

    cx, cy = 0, 0
    answer = 0
    for a in arrows:
        for _ in range(2):
            nx = cx + dx[a]
            ny = cy + dy[a]

            e1 = ((cx, cy), (nx, ny))
            e2 = ((nx, ny), (cx, cy))

            if (nx, ny) in v_node and e1 not in v_edge:
                answer += 1

            v_node.add((nx, ny))
            v_edge.add(e1)
            v_edge.add(e2)

            cx, cy = nx, ny

    print(answer)
    return answer

solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0])