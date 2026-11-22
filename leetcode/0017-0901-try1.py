# NOT Solved - Time
#
# next 개수가 많아서 전부 다 돌면 n^2이라 안될 것 같은데
# 역시 TimeLimitExceeded
#
# 연속된 낮은값을 가지고 있어야하나? - 오름차순?
# 최댓값이 들어왔을 때 다 돌지만 않는다고 해결이 될까? - 96/102 (2개 더풀었네;)
#
# 단조까진 얼추 맞았는데, 일단 오름차순이 아니고, 그것뿐만 아니라 Span을 같이 저장하고 있어야 한다?
# 내림차순으로 저장해야 더 쪼개서 저장, 오름차순 저장 시 큰 값 하나가 전부를 없애버릴 수도
#
# Try 3
class StockSpanner:

    def __init__(self):
        self.st = []

    def next(self, price: int) -> int:
        span = 1

        while self.st and self.st[-1][0] <= price:
            nxt = self.st.pop()
            span += nxt[1]
        self.st.append((price, span))

        return span


# Try 2
# class StockSpanner:
#
#     def __init__(self):
#         self.prices = []
#         self.local = 0
#
#     def next(self, price: int) -> int:
#         self.prices.append(price)
#
#         answer = 0
#         if price > self.local:
#             self.local = price
#             return len(self.prices)
#         else:
#             n = len(self.prices)
#
#             for i in range(n-1, -1, -1):
#                 if self.prices[i] <= price:
#                     answer += 1
#                 else:
#                     break
#
#             return answer


# Try 1
# class StockSpanner:
#
#     def __init__(self):
#         self.prices = []
#
#     def next(self, price: int) -> int:
#         self.prices.append(price)
#         n = len(self.prices)
#         answer = 0
#
#         for i in range(n-1, -1, -1):
#             if self.prices[i] <= price:
#                 answer += 1
#             else:
#                 break
#
#         return answer


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)


# GPT
class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1

        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]

        self.stack.append((price, span))

        return span


sol = StockSpanner()
print(sol.next())