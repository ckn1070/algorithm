# Almost Solved
# 와 진짜 거의 다 왔는데, 중앙 찾는 마지막에서 막혔다;
# 이걸 그래도 여기까지 생각해 낸게 너무 신기하네;;
#
# 무조건 정답을 가장 마지막에 한 번만 빼내겠다는 생각은 버려라
# 후보를 정답에 넣고, 그 다음으로 넘어가는거다
# 중앙값이 조건을 만족한다면, 후보에 넣고 그 다음 (중앙값은 제외하는 범위로)
#
# 일단 사람 수, 심사관 수가 굉장히 많아서 Loop 막 돌리기 시작하면 바로 끝난다
# Try 2
def solution(n, times):
    times.sort()
    left = 0
    right = times[-1] * n
    answer = right

    while left <= right:
        mid = (left + right) // 2

        cur = 0
        for i in times:
            cur += mid // i
            if cur >= n:
                print ('cur', cur)
                break

        if cur >= n:
            print('right', mid, right, left)
            answer = mid
            right = mid - 1
        else:
            print('left', mid, right, left)
            left = mid + 1

    print('ans', answer)
    return answer

# 아까운 Try 1
# def solution(n, times):
#     times.sort()
#     left = 0
#     right = times[-1] * n
#
#     while left < right:
#         mid = (left + right) // 2
#
#         cur = 0
#         for i in times:
#             cur += mid // i
#             if cur == n:
#                 print ('cur', cur)
#                 return mid
#
#         if cur >= n:
#             print('right', mid, right, left)
#             right = mid+1
#         else:
#             print('left', mid, right, left)
#             left = mid
#
#     answer = (left + right) // 2
#     print('ans', answer)
#     return answer

solution(6, [7, 10])


# Programmers
# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
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