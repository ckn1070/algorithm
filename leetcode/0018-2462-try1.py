# NOT Solved
#
# 문제 이해가 역대급으로 어려웠다
# 첫 candidate, 마지막 candidate 중에서 가장 작은 수를 뽑아내야 한다는것..
import heapq

class Solution:
    def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
        n = len(costs)
        left = 0
        right = n - 1

        heap_l = []
        heap_r = []

        for _ in range(candidates):
            if left <= right:
                heapq.heappush(heap_l, (costs[left], left))
                left += 1

            if left <= right:
                heapq.heappush(heap_r, (costs[right], right))
                right -= 1

        answer = 0

        for _ in range(k):
            if heap_l and (not heap_r or heap_l[0] <= heap_r[0]):
                answer += heapq.heappop(heap_l)[0]

                if left <= right:
                    heapq.heappush(heap_l, (costs[left], left))
                    left += 1

            else:
                answer += heapq.heappop(heap_r)[0]

                if left <= right:
                    heapq.heappush(heap_r, (costs[right], right))
                    right -= 1

        return answer



# Try 2 - 굉장히 잘못 품. 굉장히 복잡하게 풀었으며, idx를 고정해버리는 미친짓
# from collections import deque
#
# class Solution:
#     def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
#         cand = []
#         for i, cost in enumerate(costs):
#             cand.append((cost, i))
#         q = deque(sorted(cand))
#
#         answer = 0
#         for j in range(k):
#             n = len(q)
#             print(n, candidates, q)
#             if n <= 2 * candidates:
#                 print("if")
#                 answer += q.popleft()[0]
#             else:
#                 for k in range(n):
#                     nxt = q[k]
#                     if candidates <= nxt[1] < n - candidates:
#                         print("else if")
#                         continue
#                     else:
#                         print("else else")
#                         answer += nxt[0]
#                         q.remove(nxt)
#
#         return answer


# Try 1: 잘못 이해 - 131 / 164
# class Solution:
#     def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
#         cand = []
#         for i, cost in enumerate(costs):
#             cand.append((cost, i))
#         cand.sort()
#         answer = 0
#         for j in range(k):
#             answer += cand[j][0]
#
#         return answer


# GPT
# import heapq
#
#
# class Solution:
#     def totalCost(self, costs: list[int], k: int, candidates: int) -> int:
#         n = len(costs)
#
#         left_heap = []
#         right_heap = []
#
#         left = 0
#         right = n - 1
#
#         # 초기 후보자 등록
#         for _ in range(candidates):
#             if left <= right:
#                 heapq.heappush(left_heap, (costs[left], left))
#                 left += 1
#
#             if left <= right:
#                 heapq.heappush(right_heap, (costs[right], right))
#                 right -= 1
#
#         answer = 0
#
#         for _ in range(k):
#             if left_heap and (
#                     not right_heap or left_heap[0] <= right_heap[0]
#             ):
#                 cost, idx = heapq.heappop(left_heap)
#                 answer += cost
#
#                 if left <= right:
#                     heapq.heappush(left_heap, (costs[left], left))
#                     left += 1
#
#             else:
#                 cost, idx = heapq.heappop(right_heap)
#                 answer += cost
#
#                 if left <= right:
#                     heapq.heappush(right_heap, (costs[right], right))
#                     right -= 1
#
#         return answer


sol = Solution()
print(sol.totalCost([17,12,10,2,7,2,11,20,8], 3, 4))