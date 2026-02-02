# Programmers
def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer

# GPT
# from collections import deque
#
# def solution(priorities, location):
#     q = deque([(p, i) for i, p in enumerate(priorities)])
#     cnt = 0
#
#     while q:
#         p, i = q.popleft()
#         if any(p < p2 for p2, _ in q):
#             q.append((p, i))
#         else:
#             cnt += 1
#             if i == location:
#                 return cnt