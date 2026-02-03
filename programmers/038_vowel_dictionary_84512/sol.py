# GPT
def solution(word):
    order = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    weights = [781, 156, 31, 6, 1]

    ans = 0
    for i, ch in enumerate(word):
        ans += order[ch] * weights[i] + 1  # +1은 "이 글자를 선택한 단어" 자체
    return ans

# GPT
# def solution(word):
#     vowels = ['A', 'E', 'I', 'O', 'U']
#     count = 0
#     answer = 0
#
#     def dfs(current):
#         nonlocal count, answer
#         if len(current) > 5:
#             return
#
#         if current:
#             count += 1
#             if current == word:
#                 answer = count
#                 return
#
#         for v in vowels:
#             if answer:  # 이미 찾았으면 종료
#                 return
#             dfs(current + v)
#
#     dfs("")
#     return answer

