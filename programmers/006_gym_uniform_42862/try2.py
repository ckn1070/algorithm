# Solved
# 못 풀 뻔 했다
# 정렬이 없다는 가정이 없으면, 절대 정렬이 되어있을 것이라고 생각하지말기
from collections import defaultdict as dd

def solution(n, lost, reserve):
    cnt = dd(int)

    for i in sorted(lost):
        if i not in reserve:
            print('i', i)
            cnt[i] -= 1

    for j in sorted(reserve):
        if j not in lost:
            print('j', j, cnt[j-1], cnt[j+1])
            if j > 1 and cnt[j-1] < 0:
                cnt[j-1] += 1
            elif j < n and cnt[j+1] < 0:
                cnt[j+1] += 1

    answer = 0
    for k in range(n):
        print('k:', k, cnt[k])
        if cnt[k+1] >= 0:
            answer += 1
    print('answer:', answer )
    return answer

solution(5, [1, 2, 4], [2, 3, 5])
solution(5, [2, 4], [3])
solution(3, [3], [1])


# Programmers
# def solution(n, lost, reserve):
#     _reserve = [r for r in reserve if r not in lost]
#     _lost = [l for l in lost if l not in reserve]
#     for r in _reserve:
#         f = r - 1
#         b = r + 1
#         if f in _lost:
#             _lost.remove(f)
#         elif b in _lost:
#             _lost.remove(b)
#     return n - len(_lost)