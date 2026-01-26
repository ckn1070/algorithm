from collections import defaultdict

# GPT
def solution(clothes):
    kind = defaultdict(int)
    for _, j in clothes:
        kind[j] += 1

    answer = 1
    for c in kind.values():
        answer *= (c + 1)

    return answer - 1

# Programmers
# def solution(clothes):
#     clothes_type = {}
#
#     for c, t in clothes:
#         if t not in clothes_type:
#             clothes_type[t] = 2
#         else:
#             clothes_type[t] += 1
#
#     cnt = 1
#     for num in clothes_type.values():
#         cnt *= num
#
#     return cnt - 1