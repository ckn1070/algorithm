# Solved
import heapq

class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        n = len(costs)
        left = 0
        right = n - 1

        l_h = []
        r_h = []

        for _ in range(candidates):
            if left <= right:
                heapq.heappush(l_h, (costs[left], left))
                left += 1

            if left <= right:
                heapq.heappush(r_h, (costs[right], right))
                right -= 1

        answer = 0

        for _ in range(k):
            if l_h and (not r_h or l_h[0] <= r_h[0]):
                answer += heapq.heappop(l_h)[0]

                if left <= right:
                    heapq.heappush(l_h, (costs[left], left))
                    left += 1

            else:
                answer += heapq.heappop(r_h)[0]

                if left <= right:
                    heapq.heappush(r_h, (costs[right], right))
                    right -= 1

        return answer


sol = Solution()
print(sol.totalCost([17,12,10,2,7,2,11,20,8], 3, 4))