# NOT Solved
#
# 정렬을 하는 순간 nlogn이 되어버리니.. 정렬 + 스택은 안되고
# set을 만들어도 공간이 n이되려나
# 상수 몇 개로 처리해야하는데..
#
# 비트 연산 필요;;
class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        answer = 0

        for num in nums:
            answer ^= num

        return answer


# Try 1 - 시간 복잡도는 n이 맞지만, 공간 복잡도가 n (문제 조건: 1)
from collections import Counter

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        c = Counter(nums)
        for k in c.keys():
            if c[k] == 1:
                return k


sol = Solution()
print(sol.solution())