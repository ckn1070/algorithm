# GPT
def solution(triangle):
    # dp에 triangle을 복사해서 누적 최댓값으로 덮어쓰기
    dp = [row[:] for row in triangle]

    for i in range(1, len(dp)):
        for j in range(i + 1):
            if j == 0:
                # 왼쪽 끝은 위에서 내려오는 경우 1개
                dp[i][j] += dp[i-1][j]
            elif j == i:
                # 오른쪽 끝도 위에서 내려오는 경우 1개
                dp[i][j] += dp[i-1][j-1]
            else:
                # 중간은 위의 두 경로 중 큰 값
                dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

    return max(dp[-1])


# Programmers
# solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])
