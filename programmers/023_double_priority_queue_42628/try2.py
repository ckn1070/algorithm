# NOT Solved
#
# 최댓값, 최솟값 큐 링크 시키는게 문제 해결이란 것은 알겠다
# 상당히 까다로웠던 것도 기억이 난다
# 방법이 여러가지였던 것도 기억이 난다..
#
# id까지 설정하고, Lazy delete가 필요하다 - 이것이 링크하는 방법
#
# Try 2
import heapq

def solution(operations):
    mxh = []
    mnh = []
    removed = {}

    for idx, operation in enumerate(operations):
        op, val = operation.split(" ")
        val = int(val)

        if op == 'I':
            heapq.heappush(mxh, (-val, idx))
            heapq.heappush(mnh, (val, idx))

        elif op == 'D' and val == 1:
            while mxh and removed.get(mxh[0][1], False):
                heapq.heappop(mxh)
            if mxh:
                _, i = heapq.heappop(mxh)
                removed[i] = True
        else:
            while mnh and removed.get(mnh[0][1], False):
                heapq.heappop(mnh)
            if mnh:
                _, i = heapq.heappop(mnh)
                removed[i] = True

    while mxh and removed.get(mxh[0][1], False):
        heapq.heappop(mxh)
    while mnh and removed.get(mnh[0][1], False):
        heapq.heappop(mnh)

    answer = [0, 0] if not mxh or not mnh else [-mxh[0][0], mnh[0][0]]
    print(answer)
    return answer


# Try 1
# 6/10 으으.. 4개는 뭘까 대체
# import heapq
#
# def solution(operations):
#     mxq = []
#     mnq = []
#
#     cnt = 0
#     for operation in operations:
#         op, val = operation.split(" ")
#
#         if op == "I":
#             heapq.heappush(mxq, -int(val))
#             heapq.heappush(mnq, int(val))
#             cnt += 1
#
#         if op == "D" and val == "1":
#             if cnt > 0:
#                 heapq.heappop(mxq)
#                 cnt -= 1
#             # 이것도 else에서 조건을 추가했는데 아무런 효과가 없구만;
#             if cnt <= 0 or not mxq:
#                 mnq = []
#
#         if op == "D" and val == "-1":
#             if cnt > 0:
#                 heapq.heappop(mnq)
#                 cnt -= 1
#             if cnt <= 0 or not mnq:
#                 mxq = []
#
#     answer = []
#     # cnt == 0 추가했는데 아무런 효과 없구만;
#     if not mxq or not mnq or cnt == 0:
#         answer = [0, 0]
#     else:
#         answer = [-heapq.heappop(mxq), heapq.heappop(mnq)]
#
#     print('ans', cnt, mxq, mnq, answer)
#     return answer

solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])
solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])