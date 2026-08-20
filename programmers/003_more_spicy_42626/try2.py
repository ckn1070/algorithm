# Half Solved
# Heapq 떠올린 것도 늦었고, 푼 것도 찝찝하고..
import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0

    while len(scoville) > 1:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        print(first, second)
        if first >= K:
            break
        mix = first + (second * 2)
        answer += 1
        heapq.heappush(scoville, mix)

        # IF가 while 밖에 있으면 틀린다..
        if len(scoville) == 1 and scoville[0] < K:
            answer = -1
            break
        if len(scoville) == 0:
            answer = -1
            break

    print(answer)
    return answer

solution([1, 2, 3, 9, 10, 12], 7)

# GPT
# import heapq
#
#
# def solution(scoville, K):
#     heapq.heapify(scoville)
#     answer = 0
#
#     while scoville[0] < K:
#         if len(scoville) < 2:
#             return -1
#
#         first = heapq.heappop(scoville)
#         second = heapq.heappop(scoville)
#
#         mix = first + second * 2
#         heapq.heappush(scoville, mix)
#
#         answer += 1
#
#     return answer


# Programmers
# import heapq as hq
#
#
# def solution(scoville, K):
#
#     hq.heapify(scoville)
#     answer = 0
#     while True:
#         first = hq.heappop(scoville)
#         if first >= K:
#             break
#         if len(scoville) == 0:
#             return -1
#         second = hq.heappop(scoville)
#         hq.heappush(scoville, first + second*2)
#         answer += 1
#
#     return answer


# Runtime Error
#
# def solution(scoville, K):
#     scoville.sort(reverse=True)
#     answer = 0
#     print(scoville)
#
#     while len(scoville) > 1:
#         first = scoville.pop()
#         second = scoville.pop()
#         if first >= K:
#             break
#         mix = first + (second * 2)
#         scoville.append(mix)
#         answer += 1
#         scoville.sort(reverse=True)
#
#     if len(scoville) <= 1 and scoville[0] <= K:
#         answer = -1
#
#     print(answer)
#     return answer