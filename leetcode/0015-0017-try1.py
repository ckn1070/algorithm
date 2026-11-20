# Solved - 매우 힘겹게..
#
# 순서 고정을 어떻게할래? (앞에서부터)
# 이렇게 간단한 문제를 이렇게 어렵게 풀었다고..
from collections import defaultdict

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        d = defaultdict(list)
        d['2'] = ['a', 'b', 'c']
        d['3'] = ['d', 'e', 'f']
        d['4'] = ['g', 'h', 'i']
        d['5'] = ['j', 'k', 'l']
        d['6'] = ['m', 'n', 'o']
        d['7'] = ['p', 'q', 'r', 's']
        d['8'] = ['t', 'u', 'v']
        d['9'] = ['w', 'x', 'y', 'z']

        answer = set()

        def dfs(idx, word):
            if idx == len(digits):
                answer.add(word)
                return
            digit = digits[idx]
            for letter in d[digit]:
                dfs(idx + 1, word + letter)

        # visited = [False] * len(digits)
        #
        # def dfs(word):
        #     for i, digit in enumerate(digits):
        #         if not visited[i]:
        #             visited[i] = True
        #             for letter in d[digit]:
        #                 dfs(word + letter)
        #             visited[i] = False
        #         if len(word) == len(digits):
        #             answer.add(word)

        dfs(0, '')
        print(answer)
        return list(answer)


# GPT
# class Solution:
#     def letterCombinations(self, digits: str) -> list[str]:
#         if not digits:
#             return []
#
#         phone = {
#             '2': 'abc',
#             '3': 'def',
#             '4': 'ghi',
#             '5': 'jkl',
#             '6': 'mno',
#             '7': 'pqrs',
#             '8': 'tuv',
#             '9': 'wxyz'
#         }
#
#         answer = []
#         path = []
#
#         def dfs(idx):
#             if idx == len(digits):
#                 answer.append(''.join(path))
#                 return
#
#             for ch in phone[digits[idx]]:
#                 path.append(ch)
#                 dfs(idx + 1)
#                 path.pop()
#
#         dfs(0)
#         return answer



sol = Solution()
print(sol.letterCombinations())