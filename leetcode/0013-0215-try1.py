# NOT Solved
#
# 흠.. 10^5인데 n^2으로 되나
# 역시.. Time Limit Exceeded at 38/47
# 전부 다 정렬을 하는게 아니라 k번째를 찾아야겠는데
#
# 아 미친 힙 떠올렸는데 이것도 정렬이 아닌거에 들어가는구나.. 너무 아쉽다
# 힙에 replace가 있구나
#
# Try 3
import heapq

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        h = nums[:k]
        heapq.heapify(h)

        for num in nums[k:]:
            if num > h[0]:
                heapq.heapreplace(h, num)

        return h[0]


# Try 2
# class Solution:
#     def findKthLargest(self, nums: list[int], k: int) -> int:
#         st = []
#         left = []
#
#         for num in nums:
#             while st and st[-1] < num:
#                 left.append(st.pop())
#             print(st,left, left[::-1][:k - len(st)])
#             st.append(num)
#             st += left[::-1][:k - len(st)]
#             left.clear()
#         print(st)
#
#         return st[k - 1]


# Try 1
# class Solution:
#     def findKthLargest(self, nums: list[int], k: int) -> int:
#         st = []
#         left = []
#
#         for num in nums:
#             while st and st[-1] < num:
#                 left.append(st.pop())
#             st.append(num)
#             st += left[::-1]
#             left.clear()
#         print(st)
#
#         return st[k - 1]


# GPT - Heap
# import heapq
#
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         heap = nums[:k]
#         heapq.heapify(heap)
#
#         for num in nums[k:]:
#             if num > heap[0]:
#                 heapq.heapreplace(heap, num)
#
#         return heap[0]


# GPT - QuickSelect
# import random
#
# class Solution:
#     def findKthLargest(self, nums: List[int], k: int) -> int:
#         target = k - 1
#         left, right = 0, len(nums) - 1
#
#         while left <= right:
#             pivot_idx = random.randint(left, right)
#             nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
#
#             pivot = nums[right]
#             store = left
#
#             for i in range(left, right):
#                 if nums[i] > pivot:
#                     nums[store], nums[i] = nums[i], nums[store]
#                     store += 1
#
#             nums[store], nums[right] = nums[right], nums[store]
#
#             if store == target:
#                 return nums[store]
#             elif store < target:
#                 left = store + 1
#             else:
#                 right = store - 1