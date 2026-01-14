# GPT
def solution(distance, rocks, n):
    rocks.sort()

    left, right = 1, distance
    answer = 0

    while left <= right:
        mid = (left + right) // 2  # "최소 거리"를 mid 이상으로 만들 수 있는가?

        removed = 0
        prev = 0  # 출발점

        for r in rocks:
            if r - prev < mid:
                removed += 1      # 이 바위는 너무 가까우니 제거
            else:
                prev = r          # 남기고 기준점 갱신

        # 도착점까지 거리도 체크
        if distance - prev < mid:
            removed += 1

        if removed <= n:
            answer = mid          # mid 가능 -> 더 키워보기
            left = mid + 1
        else:
            right = mid - 1       # mid 불가능 -> 줄이기

    return answer

# Programmers
# def solution(distance, rocks, n):
#     answer = 0
#     sorted_rocks = sorted(rocks)
#     sorted_rocks.append(distance)
#     left = 0
#     right = distance
#     while (left <= right):
#         mid = int((left + right) / 2)
#         cnt = 0
#         p = 0
#         for i in range(len(sorted_rocks)):
#             if (sorted_rocks[i] - p < mid):
#                 cnt += 1
#             else:
#                 p = sorted_rocks[i]
#         if cnt > n:
#             right = mid - 1
#         else:
#             left = mid + 1
#             answer = mid
#     return answer