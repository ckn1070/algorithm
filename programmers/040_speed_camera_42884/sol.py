# GPT
def solution(routes):
    routes.sort(key=lambda x: x[1])  # 끝점 기준 정렬
    cam = -10**9
    answer = 0

    for l, r in routes:
        if cam < l:        # 현재 카메라가 이 구간을 커버 못함
            answer += 1
            cam = r        # 이 구간의 끝에 카메라 설치(최대한 많은 다음 구간 커버)
    return answer

# GPT 교집합
# def solution(routes):
#     routes.sort()  # 시작점 기준 정렬
#     answer = 0
#     right = None
#
#     for l, r in routes:
#         if right is None:
#             right = r
#             continue
#
#         if l > right:      # 교집합 깨짐
#             answer += 1
#             right = r
#         else:
#             right = min(right, r)  # 교집합 유지(오른쪽 끝을 좁힘)
#
#     return answer + 1 if right is not None else 0

# Programmers
# def solution(routes):
#     routes = sorted(routes, key=lambda x: x[1])
#     last_camera = -30000
#
#     answer = 0
#
#     for route in routes:
#         if last_camera < route[0]:
#             answer += 1
#             last_camera = route[1]
#
#     return answer