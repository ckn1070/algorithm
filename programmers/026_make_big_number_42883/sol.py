# GPT
def solution(number, k):
    stack = []
    removed = 0

    for ch in number:
        while stack and removed < k and stack[-1] < ch:
            stack.pop()
            removed += 1
        stack.append(ch)

    # 아직 다 못 지웠으면 뒤에서 지우기
    if removed < k:
        stack = stack[:- (k - removed)]

    return ''.join(stack)

# Programmers
# def solution(number, k):
#     stack = [number[0]]
#     for num in number[1:]:
#         while len(stack) > 0 and stack[-1] < num and k > 0:
#             k -= 1
#             stack.pop()
#         stack.append(num)
#     if k != 0:
#         stack = stack[:-k]
#     return ''.join(stack)