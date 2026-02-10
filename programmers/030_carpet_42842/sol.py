# Programmers
def solution(brown, red):
    for i in range(1, int(red**(1/2))+1):
        if red % i == 0:
            if 2*(i + red//i) == brown-4:
                return [red//i+2, i+2]

# GPT
# def solution(brown, yellow):
#     for h in range(1, int(yellow**0.5) + 1):
#         if yellow % h != 0:
#             continue
#         w = yellow // h  # w * h = yellow
#
#         if 2*w + 2*h + 4 == brown:
#             return [w + 2, h + 2]
