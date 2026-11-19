# Solved
#
# OP 할 수 있는 경우의 수가 거의 무한에 가깝지않나..?
# 전부 다 해보고 찾을 수는 없을 것 같은데
#
# 위치를 바꿀 수 있는거면,
# 개수 그룹만 맞으면 되는거 아닌가?
# 종류도 맞긴 해야겠네
from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        wc1 = Counter(word1)
        wc2 = Counter(word2)
        print(wc1.keys(), wc1.values())
        wk1 = sorted(list(wc1.keys()))
        wk2 = sorted(list(wc2.keys()))
        wv1 = sorted(list(wc1.values()))
        wv2 = sorted(list(wc2.values()))
        return wk1 == wk2 and wv1 == wv2


# GPT
# from collections import Counter
#
# class Solution:
#     def closeStrings(self, word1: str, word2: str) -> bool:
#         c1 = Counter(word1)
#         c2 = Counter(word2)
#
#         if c1.keys() != c2.keys():
#             return False
#
#         return sorted(c1.values()) == sorted(c2.values())


sol = Solution()
print(sol.closeStrings("abc", "bca"))