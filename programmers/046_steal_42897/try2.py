# NOT Solved
# 집이 너무 많아서 경우의 수를 다 나열하는건 말이 안되는 것 같고
# dp[i][j]를 i~j 최댓값이라고 하는게 말이되나
#
# 최댓값부터 넣어가는게 안될것 같다는건 직감했지만
# 0/10, 0/10 어떻게 하나도 맞은게 없네;
# 원형이니깐 꼬이는 부분이 있겠지? 사실 1-2 차이로도 최댓값은 바뀔 수 있으니..
#
# 우선 원형을 끊어야하는데, 첫 번째 집을 무조건 포함 vs 안포함으로 나누면 된다
# DP를 왼쪽에서 오른쪽으로 가면갈수록 완성해나가는 식으로
# Try 2
def solution(money):
    n = len(money)
    dp1 = [0] * n
    dp2 = [0] * n

    # 첫 번째 포함
    dp1[0] = money[0]
    dp1[1] = max(dp1[0], money[1])
    # 첫 번째 포함하려면 마지막을 무조건 빼야한다
    for i in range(2, n - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])

    # 첫 번째 제외
    dp2[0] = 0
    dp2[1] = money[1]
    # 첫 번째 제외했기때문에 마지막 집 들어가도 된다
    for i in range(2, n):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])

    print(dp1, dp2)
    answer = max(dp1[n-2], dp2[n-1])
    return answer


# Try 1
# def solution(money):
#     home = []
#     visited = set()
#     n = len(money)
#     for i, m in enumerate(money):
#         home.append((m, i))
#     home.sort(key=lambda x: (-x[0], x[1]))
#     print(home)
#
#     answer = 0
#     for mo, ho in home:
#         left = n - 1 if ho == 0 else ho - 1
#         right = 0 if ho == n - 1 else ho + 1
#         if left not in visited and right not in visited:
#             visited.add(ho)
#             answer += mo
#
#     print(visited, answer)
#     return answer

solution([1, 2, 3, 1])