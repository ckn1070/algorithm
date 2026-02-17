# GPT
def solution(arr):
    # 1) parse
    nums = list(map(int, arr[::2]))
    ops = arr[1::2]
    n = len(nums)

    INF = 10**18
    dpMax = [[-INF] * n for _ in range(n)]
    dpMin = [[ INF] * n for _ in range(n)]

    # 2) base
    for i in range(n):
        dpMax[i][i] = nums[i]
        dpMin[i][i] = nums[i]

    # 3) length from 2..n
    for length in range(2, n + 1):
        for i in range(0, n - length + 1):
            j = i + length - 1

            best_max = -INF
            best_min =  INF

            for k in range(i, j):
                op = ops[k]
                left_max, left_min = dpMax[i][k], dpMin[i][k]
                right_max, right_min = dpMax[k + 1][j], dpMin[k + 1][j]

                if op == '+':
                    cand_max = left_max + right_max
                    cand_min = left_min + right_min
                else:  # '-'
                    cand_max = left_max - right_min
                    cand_min = left_min - right_max

                if cand_max > best_max:
                    best_max = cand_max
                if cand_min < best_min:
                    best_min = cand_min

            dpMax[i][j] = best_max
            dpMin[i][j] = best_min

    return dpMax[0][n - 1]


print(solution(["1", "-", "3", "+", "5", "-", "8"]))      # 기대: 1
print(solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"]))  # 테스트


# Programmers
# def solution(arr):
#     arrs = ''.join(arr).split('-')
#     val0 = sum(list(map(int, arrs[0].split('+'))))
#     if len(arrs) == 1:
#         return val0
#
#     min_val = 0
#     max_val = 0
#     for arr in arrs[:0:-1]:
#         x = list(map(int, arr.split('+')))
#         _min_val = -(sum(x))
#         _max_val = sum(x[1:]) - x[0]
#         min_val, max_val = min(_min_val + min_val, _min_val - max_val), max(_max_val + max_val, _min_val - min_val)
#
#     return val0 + max_val