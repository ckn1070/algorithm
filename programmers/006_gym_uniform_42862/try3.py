# Solved - 풀긴풀었는데 왜이렇게 복잡하게풀지..?
# 25/30 - 정답
from collections import defaultdict

# Try 2
def solution(n, lost, reserve):
    d = defaultdict(int)
    for i in range(1, n + 1):
        d[i] += 1
    for l in lost:
        d[l] -= 1
    for r in reserve:
        d[r] += 1
    print(d)

    answer = 0
    for k in range(1, n + 1):
        if k > 1 and d[k] > 1 and d[k - 1] <= 0:
            d[k - 1] += 1
            d[k] -= 1
            answer += 2
            print('bf', k)
        elif k < n and d[k] > 1 and d[k + 1] <= 0:
            d[k + 1] += 1
            d[k] -= 1
            answer += 1
            print('af', k)
        else:
            if d[k] > 0:
                answer += 1
                print(k)
    #     print(k,d, answer)
    print(d, answer)
    return answer

# Try 1
# def solution(n, lost, reserve):
#     d = defaultdict(int)
#     for i in range(1, n + 1):
#         d[i] += 1
#     for l in lost:
#         d[l] -= 1
#     for r in reserve:
#         if d[r] > 0:
#             if r > 1 and d[r - 1] <= 0:
#                 d[r - 1] += 1
#             elif r < n and d[r + 1] <= 0:
#                 d[r + 1] += 1
#             else:
#                 d[r] += 1
#         else:
#             d[r] += 1
#
#     answer = 0
#     for k in d.keys():
#         if d[k] > 0:
#             answer += 1
#     print(answer)
#     return answer

solution(5, [2, 4], [1, 3, 5])
solution(5, [2, 4], [3])
solution(3, [3], [1])