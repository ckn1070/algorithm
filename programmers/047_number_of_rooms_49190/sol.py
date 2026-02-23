# GPT
def solution(arrows):
    # 8방향: 0~7
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    x, y = 0, 0
    visited_nodes = {(x, y)}
    visited_edges = set()

    rooms = 0

    for d in arrows:
        # 교차 처리를 위해 한 칸 이동을 2번(반 칸 2번) 수행
        for _ in range(2):
            nx, ny = x + dx[d], y + dy[d]

            e1 = ((x, y), (nx, ny))
            e2 = ((nx, ny), (x, y))  # 무방향 간선 처리

            # "새로운 간선"으로 "이미 방문한 정점"에 들어가면 방이 1개 생김
            if (nx, ny) in visited_nodes and e1 not in visited_edges:
                rooms += 1

            visited_nodes.add((nx, ny))
            visited_edges.add(e1)
            visited_edges.add(e2)

            x, y = nx, ny

    return rooms

print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))


# Programmers
# def solution(arrows):
#     point=set([(0,0)])
#     line=set()
#     move=[[0,2],[2,2],[2,0],[2,-2],[0,-2],[-2,-2],[-2,0],[-2,2]]
#     pre_point=(0,0)
#     for A in arrows:
#         next_point=(pre_point[0]+move[A][0],  pre_point[1]+move[A][1] )
#         mid_point=(pre_point[0]+move[A][0]//2,  pre_point[1]+move[A][1]//2 )
#         point.add(next_point)
#         point.add(mid_point)
#         line.add((pre_point,mid_point))
#         line.add((mid_point,pre_point))
#         line.add((mid_point,next_point))
#         line.add((next_point,mid_point))
#         pre_point=next_point
#     answer = len(line)//2-len(point)+1
#     return answer if answer>=0 else 0