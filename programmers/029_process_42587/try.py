# Solved
from collections import deque

def solution(priorities, location):
    arr = []
    for i, v in enumerate(priorities):
        arr.append((v, i))
    q = deque(arr)

    answer = 0
    cnt = 0
    while q:
        cur = q.popleft()
        left = sorted(q, reverse=True)
        print(q, left)

        pas = True
        if not left or cur[0] >= left[0][0]:
            cnt+=1
        else:
            q.append(cur)
            pas = False

        if pas and cur[1] == location:
            answer = cnt
            break

    print(answer)
    return answer

solution([2, 1, 3, 2], 2)
solution([1, 1, 9, 1, 1, 1], 0)