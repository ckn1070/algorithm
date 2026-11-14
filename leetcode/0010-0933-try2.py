# Solved
from collections import deque

class RecentCounter:

    times = deque()

    def __init__(self):
        self.times = deque()

    def ping(self, t: int) -> int:
        self.times.append(t)

        while self.times:
            if self.times[0] < t - 3000:
                self.times.popleft()
            else:
                break

        return len(self.times)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)