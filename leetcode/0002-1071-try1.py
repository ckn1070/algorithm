# Solved
# GCD 자체가 라이브러리로 있네
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        answer = ""
        n = len(str1)
        m = len(str2)
        for i in range(n):
            if n % (i + 1) != 0 or m % (i + 1) != 0:
                continue

            tmp = str1[:i + 1]
            if tmp * (n // (i + 1)) == str1 and tmp * (m // (i + 1)) == str2:
                answer = tmp

        return answer


# GPT
# from math import gcd
#
# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         if str1 + str2 != str2 + str1:
#             return ""
#
#         length = gcd(len(str1), len(str2))
#         return str1[:length]