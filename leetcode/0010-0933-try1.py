# Solved
#
# 뭔데 이 쉬운 문제를 이렇게 오래 걸리고 어렵게 풀지...?
# Easy인데다, 내가 봐도 그리 어렵지 않아보이는데..
#
# GPT 풀이보니깐 현타오네
# 어차피 자기자신이 t이니깐 t보다 큰 건 말이 안되고
# 작은것만 다 쳐내면 되네 그냥 처음부터 큐에 넣어버리고
from collections import deque

# Try 2
class RecentCounter:

    q = deque([])

    def __init__(self):
        self.q = deque([])


    def ping(self, t: int) -> int:
        if len(self.q) == 0:
            self.q.append(t)
            return 1

        while self.q:
            print('t', t)
            if self.q[-1] < t - 3000 or self.q[-1] > t:
                print('right', self.q)
                self.q.pop()
                if len(self.q) == 0:
                    self.q.append(t)
                    return 1
                continue
            if self.q[0] < t - 3000 or self.q[0] > t:
                print('left', self.q)
                self.q.popleft()
                if len(self.q) == 0:
                    self.q.append(t)
                    return 1
                continue

            self.q.append(t)
            print('none', t, self.q)
            return len(self.q)


# GPT
# from collections import deque
#
# class RecentCounter:
#
#     def __init__(self):
#         self.q = deque()
#
#     def ping(self, t: int) -> int:
#         self.q.append(t)
#
#         while self.q[0] < t - 3000:
#             self.q.popleft()
#
#         return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)


# Try 1
# class RecentCounter:
#     times = []
#
#     def __init__(self):
#         self.times = []
#
#     def ping(self, t: int) -> int:
#         print(self.times, t)
#         n = len(self.times)
#         if n == 0:
#             self.times.append(t)
#             return 1
#
#         for i in range(n):
#             tmp = self.times[n - 1 - i]
#             if t - 3000 <= tmp <= t:
#                 self.times.append(t)
#                 return n - i + 1
#
#             self.times.append(t)