import heapq
from collections import deque

# Solved
# def solution(operations):
#     max_heap = []
#     min_heap = []
#     cnt = 0
#
#     for i in operations:
#         op = i.split(' ')
#         if op[0] == 'I':
#             heapq.heappush(min_heap, int(op[1]))
#             heapq.heappush(max_heap, -int(op[1]))
#             cnt += 1
#         if op[0] == 'D':
#             if int(op[1]) < 0:
#                 heapq.heappop(min_heap)
#             else:
#                 heapq.heappop(max_heap)
#
#
#     print('heap', min_heap, max_heap)
#     if len(max_heap) + len(min_heap) <= cnt:
#         answer = [0, 0]
#     else:
#         answer = [-(heapq.heappop(max_heap)), heapq.heappop(min_heap)]
#
#     print(answer)
#     return answer

def solution(operations):
    arr = []

    for i in operations:
        op = i.split(' ')
        if op[0] == 'I':
            arr.append(int(op[1]))
        if op[0] == 'D':
            if len(arr) == 0:
                continue

            q = deque(sorted(arr))
            if int(op[1]) < 0:
                q.popleft()
            else:
                q.pop()
            arr = list(q)

    print(arr)
    if len(arr) == 0:
        answer = [0, 0]
    elif len(arr) == 1:
        answer = [arr[0], arr[0]]
    else:
        q = deque(sorted(arr))
        answer = [q.pop(), q.popleft()]

    print('answer', answer)
    return answer

solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"])
solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])