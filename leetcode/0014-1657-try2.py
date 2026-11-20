# Solved
from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        wc1 = Counter(word1)
        wc2 = Counter(word2)

        if wc1.keys() != wc2.keys():
            return False

        return sorted(wc1.values()) == sorted(wc2.values())


sol = Solution()
print(sol.closeStrings("abc", "bca"))