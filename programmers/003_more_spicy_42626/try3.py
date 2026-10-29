# Solved - Done
import heapq

def solution(scoville, K):
    q = scoville.copy()
    heapq.heapify(q)

    answer = 0
    while q:
        cur = heapq.heappop(q)
        if cur >= K:
            break
        if not q:
            answer = -1
            break
        else:
            nxt = heapq.heappop(q)
            score = cur + nxt * 2
            print('score', cur, nxt, score)
            heapq.heappush(q, score)
            answer += 1

    print(answer)
    return answer

solution([1, 2, 3, 9, 10, 12], 7)