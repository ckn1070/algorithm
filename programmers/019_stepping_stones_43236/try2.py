# NOT Solved
#
# 돌을 n개 뺐을 때 (생기는 모든 경우의 수 중), (각각) 최소거리 (가 있을텐데) 의, 최댓값
# n개 빼는 모든 경우의 수를 계산하는 건 불가능 (바위 50,000개)
# 아예 최댓값을 상정해두고, 그거보다 작으면 돌을 빼버리기? (최솟값이 쵀대값이 되어야하니)
#
# Heap 아니면 Binary인 것 같은데, 동적으로 변하는게 아니라 Binary인가
# diff에서 붙어있는 2개를 더하면 돌을 하나 뺀 효과인데..
#
# Try 2
def solution(distance, rocks, n):
    left, right = 0, distance
    rocks.sort()

    answer = 0
    # mid: 최솟값 중 최댓값
    # 커질수록 remove 많이된다
    while left <= right:
        mid = (left + right) // 2

        removed, prev = 0, 0

        for r in rocks:
            if r - prev < mid:
                removed += 1
            else:
                prev = r

        if distance - prev < mid:
            removed += 1

        print('mid', mid, removed)

        if removed <= n:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
        print(left, right)

    print(left, right, answer)
    return answer


# Try 1
# def solution(distance, rocks, n):
#     left = 0
#     right = distance
#
#     rocks.sort()
#     diff = []
#     for i in range(len(rocks) + 1):
#         if i == 0:
#             diff.append(rocks[i] - 0)
#         elif i == len(rocks):
#             diff.append(distance - rocks[i - 1])
#         else:
#             diff.append(rocks[i] - rocks[i-1])
#     print(rocks, diff)
#
#     answer = 0
#     return answer

solution(25, [2, 14, 11, 21, 17], 2)