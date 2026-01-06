# Solved

from collections import deque
import math

def solution(progresses, speeds):
    rest = []
    for i in range(len(progresses)):
        rest.append(math.ceil((100 - progresses[i]) / speeds[i]))

    dq = deque(rest)
    print(dq)
    answer = []
    cur = dq.popleft()
    counter = 1
    while len(dq) > 0:
        nxt = dq.popleft()
        if cur >= nxt:
            print('1:', cur, nxt, counter)
            counter += 1
        else:
            print('2:', cur, nxt, counter)
            answer.append(counter)
            counter = 1
            cur = nxt

    if counter > 0:
        answer.append(counter)

    print(answer)
    return answer

# answer = []
    # while len(dq) > 0:
    #     target = math.ceil(100 - dq[0] / speeds[0])
    #
    #     for i in range(len(dq)):
    #         dq[i] += speeds[i] * target
    #
    #     rest = []
    #     counter = 0
    #     while len(dq) > 0:
    #         cur = dq.popleft()
    #         if cur >= 100:
    #             counter += 1
    #         else:
    #             rest.append(cur)
    #
    #     if len(rest) > 0:
    #         dq = deque(rest)
    #     if counter > 0:
    #         answer.append(counter)
    #
    # print(answer)
    # return answer

solution([93, 30, 55], [1, 30, 5])
solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])