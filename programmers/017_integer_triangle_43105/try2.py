# NOT Solved
#
# 각 층별 최댓값을 이어가면 되나 했는데, 아랫층에서 최댓값이 계속 나올수도 (1 다음 계속 8만 나올수도)
# 한 층당 2의 거듭제곱이라 모든 경우의 수를 계산하기는 불가능
#
# 층별로 미리 계산을 해서 다음 레벨로 내려주면 되는데, 특정 노드에는 하나 이상 값이 필요하다
# 이걸 어떻게 구현해야 할지가 너무 까다롭네
#
# 복사하는 것까지도 맞긴 했는데.. 왜이렇게 복잡하게 풀었을까;
# 중간은 여러개를 다 저장하는게 아니라, 가능한 가장 큰 값만 하면 된다
# 생각해보니 어차피 어떤 경로로 왔는지는 알 바가 아닌걸?
#
# Try 2
def solution(triangle):
    dp = [row[:] for row in triangle]

    for i in range(1, len(dp)):
        for j in range(0, len(dp[i])):
            if j == 0:
                dp[i][j] += dp[i-1][0]
            elif j == len(dp[i])-1:
                dp[i][j] += dp[i-1][len(dp[i])-2]
            else:
                dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])


    print(dp)
    answer = max(dp[-1])
    print(answer)
    return answer


# Try 1
# import copy
# def solution(triangle):
#     print(triangle)
#
#     dp = copy.deepcopy(triangle)
#     for i, level in enumerate(dp):
#         for j, node in enumerate(level):
#             dp[i][j] = []
#     dp[0][0].append(triangle[0][0])
#
#     for i, level in enumerate(triangle):
#         print(dp)
#         for j, node in enumerate(level):
#             if i < len(triangle) - 1:
#
#
#
#     answer = 0
#     return answer


# Programmers
# solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])


solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])