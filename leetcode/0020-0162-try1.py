# NOT Solved
#
# logn이면 한 번 다 도는것도 안되네
# binary가 말이 되나? 어떤 쪽을 선택할 줄 알고?
#
# 범위 밖의 원소가 무조건 작다는 보장이 있으니깐 가능하네..
# 계속 오르막이면 오른쪽에 무조건 있고, 계속 내리막이면 왼쪽에 무조건 있네
#
# 이건 뭔가 프로그래머스 이진이랑 느낌이 좀 많이 다르네
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left

# Try 2
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        if nums[left] > nums[left + 1]:
            return left
        if nums[right] > nums[right - 1]:
            return right

        while left <= right:
            mid = (left + right) // 2
            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return right




# Try 1
# class Solution:
#     def findPeakElement(self, nums: list[int]) -> int:
#         left, right = 0, len(nums) - 1
#
#         if nums[left] > nums[left + 1]:
#             return left
#         if nums[right] > nums[right - 1]:
#             return right
#
#         while left <= right:
#             mid = (left + right) // 2
#
#             if nums[mid - 1] < nums[mid] > nums[mid + 1]:
#                 return mid
#
#             if nums[mid - 1] > nums[mid]:
#                 left = mid + 1
#             elif nums[mid + 1] > nums[mid]:
#                 right = mid - 1


# GPT
# class Solution:
#     def findPeakElement(self, nums: list[int]) -> int:
#         left = 0
#         right = len(nums) - 1
#
#         while left < right:
#             mid = (left + right) // 2
#
#             if nums[mid] < nums[mid + 1]:
#                 left = mid + 1
#             else:
#                 right = mid
#
#         return left


sol = Solution()
print(sol.solution())