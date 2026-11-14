# Solved - 상당히 간단하게 풀었네;
# Medium 내에서도 왜이렇게 난이도 차이가 큰 것 같지..

class Solution:
    def removeStars(self, s: str) -> str:
        n = len(s)

        answer = []

        for i in range(n):
            if s[i] == '*':
                answer.pop()
            else:
                answer.append(s[i])

        return ''.join(answer)


# GPT
# class Solution:
#     def removeStars(self, s: str) -> str:
#         stack = []
#
#         for ch in s:
#             if ch == '*':
#                 stack.pop()
#             else:
#                 stack.append(ch)
#
#         return ''.join(stack)