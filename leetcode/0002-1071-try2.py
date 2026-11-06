# Solved - 근데 어째.. 전보다 더 못 푼 것 같냐 실력이 더 퇴화해
# gcd import 할 수 없다는데? 이거 gpt가 추천해준거였는데
# Try 2
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        if str1 + str2 != str2 + str1:
            return ""

        if str1 == str2:
            return str1

        n, m = len(str1), len(str2)
        answer = ""
        i = 0
        while i * 2 <= max(n, m):
            if n % (i+1) != 0 or m % (i+1) != 0:
                i += 1
                continue

            com = str(str1[:i + 1])
            print(i, com, com * (n // (i+1)), com * (m // (i+1)))
            if com * (n // (i + 1)) == str1 and com * (m // (i + 1)) == str2:
                answer = com

            i += 1

        return answer


# Try 1
# from math import gcd
# class Solution(object):
#     def gcdOfStrings(self, str1, str2):
#         """
#         :type str1: str
#         :type str2: str
#         :rtype: str
#         """
#
#         if str1 + str2 != str2 + str1:
#             return ""
#
#         com = gcd(len(str1), len(str2))
#         return str1[:com + 1] if str1[: com + 1] == str2[: com + 1] else ""