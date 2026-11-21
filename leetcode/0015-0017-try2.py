# Solved
#
# 진짜 미치겠네. 똑같은거 또 푸는데 똑같이 또 막혀이걸?
#
# 위치를 찍어주고, 다음 위치를 넘겨주는 인자가 꼭 필요
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        d = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }
        n = len(digits)
        answer = set()

        def dfs(i, word):
            if i == n:
                answer.add(word)
                return

            digit = digits[i]
            for ch in d[digit]:
                dfs(i + 1, word + ch)


        dfs(0, '')
        return list(answer)


# GPT - 백트래킹 방식으로 풀어보기
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        d = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        n = len(digits)
        visited = []
        answer = []

        def dfs(idx):
            if idx == n:
                answer.append("".join(visited))
                return

            digit = digits[idx]
            for ch in d[digit]:
                visited.append(ch)
                dfs(idx + 1)
                visited.pop()

        dfs(0)
        print(answer)
        return answer