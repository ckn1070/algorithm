# Programmers
# def solution(prices):
#     stack = []
#     answer = [0] * len(prices)
#     for i in range(len(prices)):
#         if stack != []:
#             while stack != [] and stack[-1][1] > prices[i]:
#                 past, _ = stack.pop()
#                 answer[past] = i - past
#         stack.append([i, prices[i]])
#     for i, s in stack:
#         answer[i] = len(prices) - 1 - i
#     return answer


# GPT
# def solution(prices):
#     n = len(prices)
#     ans = [0] * n
#     stack = []  # index만 저장 (prices[stack[-1]]로 값 접근)
#
#     for i in range(n):
#         # 현재 가격이 더 낮아지는 순간, 스택 top들은 "떨어짐"이 확정
#         while stack and prices[stack[-1]] > prices[i]:
#             j = stack.pop()
#             ans[j] = i - j
#         stack.append(i)
#
#     # 끝까지 안 떨어진 애들 처리
#     while stack:
#         j = stack.pop()
#         ans[j] = (n - 1) - j
#
#     return ans