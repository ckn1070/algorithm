# NOT Solved
#
# 길이가 굉장히 큰 것을 보니 모든 경우의 수를 다 찾는것은 불가하고..
# 로직을 찾아야할 것 같은데
#
# 최솟값 트레킹이 의미가 있나?
#
# 역시 n^2 들어가니, TimeLimitExceed..
#
# Idx가 꼬일 수는 있으나, 그렇다 해도 first < second가 idx 순서대로 존재했던 쌍이 과거에 있었다는 사실은 부정되지 않음
class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        f = 10**18
        s = 10**18

        for num in nums:
            if num <= f:
                f = num
            elif num <= s:
                s = num
            else:
                return True

        return False


# Try 1 - 78/88
# class Solution:
#     def increasingTriplet(self, nums: list[int]) -> bool:
#         st = []
#         n = len(nums)
#
#         for i, num in enumerate(nums):
#             st.append((num, i))
#         st.sort(key=lambda x: (x[0], x[1]))
#         print('st', st)
#
#         for j in range(n):
#             cnt = 1
#             mx = st[j][0]
#             mxi = st[j][1]
#             for k in range(j, n):
#                 if st[k][0] > mx and st[k][1] > mxi:
#                     cnt += 1
#                     mx = st[k][0]
#                     mxi = st[k][1]
#                     print(j, k, cnt)
#                 if cnt >= 3:
#                     return True
#         return False


# GPT
# class Solution:
#     def increasingTriplet(self, nums: list[int]) -> bool:
#         first = float('inf')
#         second = float('inf')
#
#         for num in nums:
#             if num <= first:
#                 first = num
#
#             elif num <= second:
#                 second = num
#
#             else:
#                 return True
#
#         return False



sol = Solution()
print(sol.increasingTriplet([2,1,5,0,4,6]))
print(sol.increasingTriplet([0,4,2,1,0,-1,-3]))
print(sol.increasingTriplet([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]))