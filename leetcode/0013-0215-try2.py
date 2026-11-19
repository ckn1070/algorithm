# Solved
#
import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        h = nums[:k]
        heapq.heapify(h)

        for num in nums[k:]:
            if num > h[0]:
                heapq.heapreplace(h, num)

        return h[0]