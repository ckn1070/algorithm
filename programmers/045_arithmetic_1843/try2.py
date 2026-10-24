# NOT Solved
# 역시 싹 다 돌리니 시간초과 나는구만
# 우선 이렇게 기본 정답은 맞긴 했는데;;
# 저번 연산도 DP였는데, 이것도 DP로 풀어야하나보다
# Try 2
def solution(arr):
    INF = 10**18
    nums = list(map(int, arr[::2])) # Number만 다 잘라주기
    ops = arr[1::2] # OPs만 다 잘라주기
    n = len(nums)
    print(nums, ops, n)

    # -를 할 때에는 최솟값을 빼야해서, 최대dp와 최소dp를 모두 관리해야한다
    # dp[i][j]는 i부터 j까지 계산했을 때의 극값을 나타낸다
    min_dp = [[INF] * n for _ in range(n)]
    max_dp = [[-INF] * n for _ in range(n)]

    for idx in range(n):
        min_dp[idx][idx] = nums[idx]
        max_dp[idx][idx] = nums[idx]

    # 길이는 2부터 시작해서 n까지 (숫자 2개 계산 ~ 숫자 n개 계산)
    for l in range(2, n + 1):
        # i는 시작값, 길이만큼 뺀 idx가 시작값의 최대
        for i in range(n - l + 1):
            # j는 해당 길이의 끝값
            j = i + l - 1

            gl_max = -INF
            gl_min = INF
            # k는 그 사이 자르는 위치 (묶여있는 두 그룹의 최종 연산)
            for k in range(i, j):
                op = ops[k]
                l_max, l_min = max_dp[i][k], min_dp[i][k]
                r_max, r_min = max_dp[k+1][j], min_dp[k+1][j]

                if op == '+':
                    lo_max = l_max + r_max
                    lo_min = l_min + r_min
                else:
                    lo_max = l_max - r_min
                    lo_min = l_min - r_max

                if lo_max > gl_max:
                    gl_max = lo_max
                if lo_min < gl_min:
                    gl_min = lo_min

            min_dp[i][j] = gl_min
            max_dp[i][j] = gl_max
            print(max_dp, min_dp)

    answer = max_dp[0][n-1]
    return answer


# Try 1
# def solution(arr):
#     total = set()
#
#     def dfs(in_arr):
#         for i in range(1, len(in_arr), 2):
#             ar = in_arr[i - 1] + in_arr [i] + in_arr[i + 1]
#             cur = [str(eval(ar))]
#             left = in_arr[:i-1] if i > 0 else []
#             right = in_arr[i+2:] if i < len(in_arr) - 2 else []
#             nxt = left + cur + right
#             print('i', i, ar, cur, left, right, left+right, nxt)
#
#             if len(nxt) == 1:
#                 total.add(int(nxt[0]))
#                 break
#             else:
#                 dfs(nxt)
#
#     dfs(arr)
#     print(total, max(total))
#     return max(total)

solution(["1", "-", "3", "+", "5", "-", "8"])
solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"])
