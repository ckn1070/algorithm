# NOT Solved

import heapq

def solution(jobs):
    q = []
    for i in range(len(jobs)):
        heapq.heappush(q, jobs[i][::-1])

    start = 0
    dur = []
    while len(q) > 0:
        cur = heapq.heappop(q)
        if start < cur[1]:
            start = cur[1]
        start = start + cur[0]
        dur.append(start - cur[1])
        print('cur:', start, cur[0], cur[1])

    answer = sum(dur) // len(dur)
    print(dur)
    print(answer)
    return answer

solution([[0, 3], [1, 9], [3, 5]])
solution([[0, 3], [5, 9], [12, 5]])