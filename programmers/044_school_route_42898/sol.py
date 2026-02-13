# GPT
# def solution(m, n, puddles):
#     MOD = 1_000_000_007
#
#     puddle = set(map(tuple, puddles))  # (x,y)
#     dp = [[0] * (m + 1) for _ in range(n + 1)]  # dp[y][x]로 쓸게요 (행= y)
#
#     dp[1][1] = 1
#
#     for y in range(1, n + 1):
#         for x in range(1, m + 1):
#             if (x, y) in puddle:
#                 dp[y][x] = 0
#                 continue
#             if x == 1 and y == 1:
#                 continue
#             dp[y][x] = (dp[y][x - 1] + dp[y - 1][x]) % MOD
#
#     return dp[n][m]
#
# print(solution(4, 3, [[2, 2]]))  # 4


# Programmers
# def solution(m,n,puddles):
#     grid = [[0]*(m+1) for i in range(n+1)] #왼쪽, 위로 한줄씩 만들어서 IndexError 방지
#     if puddles != [[]]:                    #물이 잠긴 지역이 0일 수 있음
#         for a, b in puddles:
#             grid[b][a] = -1                #미리 -1로 체크
#     grid[1][1] = 1
#     for j in range(1,n+1):
#         for k in range(1,m+1):
#             if j == k == 1:                #(1,1)은 1로 만들어두고, 0이 되지 않도록
#                 continue
#             if grid[j][k] == -1:           #웅덩이는 0으로 만들어 다음 덧셈 때 영향끼치지 않게
#                 grid[j][k] = 0
#                 continue
#             grid[j][k] = (grid[j][k-1] + grid[j-1][k])%1000000007   #[a,b] = [a-1,b] + [a,b-1] 공식
#
#     return grid[n][m]
