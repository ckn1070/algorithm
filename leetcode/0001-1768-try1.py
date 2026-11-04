# Solved
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        n = len(word1)
        m = len(word2)
        l = max(n, m)
        answer = ''

        for i in range(l):
            if i <= n - 1:
                answer += word1[i]
            if i <= m - 1:
                answer += word2[i]

        return answer


# GPT
# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         answer = []
#         n = min(len(word1), len(word2))
#
#         for i in range(n):
#             answer.append(word1[i])
#             answer.append(word2[i])
#
#         answer.append(word1[n:])
#         answer.append(word2[n:])
#
#         return ''.join(answer)