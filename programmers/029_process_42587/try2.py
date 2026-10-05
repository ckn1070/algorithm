# Solved
# any 기능을 전혀 모르니 이렇게 어렵게풀지;
from collections import deque

def solution(priorities, location):
    q = deque()
    s = set()
    prio = []

    for i, p in enumerate(priorities):
        s.add(i)
        prio.append(p)
        q.append((i, p))
    prio.sort()

    answer = 0
    while q:
        ci, cp = q.popleft()
        np = prio.pop()
        print('q', ci, cp, np)
        if cp == np:
            answer += 1
            if ci == location:
                print('ans', answer)
                return answer
        else:
            prio.append(np)
            q.append((ci, cp))

    return answer

solution([2, 1, 3, 2], 2)
solution([1, 1, 9, 1, 1, 1]	, 0)