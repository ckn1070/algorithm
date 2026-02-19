# GPT
def rob_linear(arr):
    prev2, prev1 = 0, 0  # dp[i-2], dp[i-1]
    for x in arr:
        prev2, prev1 = prev1, max(prev1, prev2 + x)
    return prev1

def solution(money):
    n = len(money)
    if n == 1:
        return money[0]
    # 0번 포함(마지막 제외) vs 0번 제외(마지막 포함)
    return max(rob_linear(money[:-1]), rob_linear(money[1:]))

print(solution([1, 2, 3, 1]))  # 4

# Programmers
# def solution(a):
#     x1, y1, z1 = a[0], a[1], a[0]+a[2]
#     x2, y2, z2 = 0, a[1], a[2]
#     for i in a[3:]:
#         x1, y1, z1 = y1, z1, max(x1, y1)+i
#         x2, y2, z2 = y2, z2, max(x2, y2)+i
#     return max(x1, y1, y2, z2)
