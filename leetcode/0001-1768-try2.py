# Solved
class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        answer = ""
        cur = 0
        for i in range(min(len(word1), len(word2))):
            answer += word1[i]
            answer += word2[i]
            cur = i

        return answer + word1[cur + 1:] if len(word1) > len(word2) else answer + word2[cur + 1:]
