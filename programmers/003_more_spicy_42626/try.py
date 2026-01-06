# Solved
import heapq


def solution(scoville, K):
    heapq.heapify(scoville)
    print(scoville)

    counter = 0

    while True:
        if len(scoville) < 2:
            if scoville[0] < K:
                counter = -1
            break

        first = heapq.heappop(scoville)

        if first >= K:
            break

        second = heapq.heappop(scoville)
        merge = first + (second * 2)
        print('sco', scoville)
        print('count', counter)

        if merge < first:
            counter = -1
            break
        else:
            counter += 1
            heapq.heappush(scoville, merge)

    answer = counter

    print(answer)
    return answer

solution([1, 2, 3, 9, 10, 12], 7)