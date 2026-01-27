# NOT Solved
from collections import deque

def solution(people, limit):
    q = deque(sorted(people))

    answer = 1
    boat = 0
    cnt = 0
    while q:
        cur = q[0]
        print(cur)

        if cnt < 2 and boat + cur <= limit:
            boat += q.popleft()
            cnt +=1
            continue
        else:
            boat = 0
            cnt = 0
            answer += 1

    print(answer)
    return answer

solution([70, 50, 80, 50], 100)
solution([70, 80, 50], 100)