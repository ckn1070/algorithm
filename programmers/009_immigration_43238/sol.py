# GPT
def solution(n, times):
    times.sort()  # 정렬 (가장 빠른 심사관부터)

    left = 1
    right = times[-1] * n  # 가장 느린 심사관이 n명 다 맡는 최악의 경우
    answer = right

    while left <= right:
        mid = (left + right) // 2  # mid 분 안에 몇 명을 처리할 수 있는지 확인
        people = 0

        for t in times:
            people += mid // t
            if people >= n:  # 이미 n명 이상 처리 가능하면 더 볼 필요 없음
                break

        if people >= n:
            # mid 시간 안에 n명 처리 가능 -> 시간을 더 줄여본다
            answer = mid
            right = mid - 1
        else:
            # mid 시간으로는 부족 -> 시간을 늘려야 한다
            left = mid + 1

    return answer

# Programmers
# def solution(n, times):
#     answer = 0
#     start, end, mid = 1, times[-1] * n, 0
#
#     while start < end:
#         mid = (start + end) // 2
#         total = 0
#         for time in times:
#             total += mid // time
#
#         if total >= n:
#             end = mid
#         else:
#             start = mid + 1
#     answer = start
#     return answer