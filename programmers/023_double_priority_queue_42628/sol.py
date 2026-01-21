import heapq

# GPT
def solution(operations):
    min_heap = []  # (value, id)
    max_heap = []  # (-value, id)
    alive = {}     # id -> True/False
    uid = 0

    def purge_min():
        while min_heap and not alive.get(min_heap[0][1], False):
            heapq.heappop(min_heap)

    def purge_max():
        while max_heap and not alive.get(max_heap[0][1], False):
            heapq.heappop(max_heap)

    for op in operations:
        cmd, num = op.split()
        num = int(num)

        if cmd == 'I':
            alive[uid] = True
            heapq.heappush(min_heap, (num, uid))
            heapq.heappush(max_heap, (-num, uid))
            uid += 1

        else:  # cmd == 'D'
            if num == 1:
                purge_max()
                if max_heap:
                    _, id_ = heapq.heappop(max_heap)
                    alive[id_] = False
            else:  # num == -1
                purge_min()
                if min_heap:
                    _, id_ = heapq.heappop(min_heap)
                    alive[id_] = False

    # 최종 정리 후 결과 뽑기
    purge_min()
    purge_max()

    if not min_heap or not max_heap:
        return [0, 0]

    max_val = -max_heap[0][0]
    min_val = min_heap[0][0]
    return [max_val, min_val]


# Gemini
# import heapq
#
# def solution(operations):
#     min_heap = []
#     max_heap = []
#     visited = [False] * 1000001  # 각 연산의 유효성 체크 (최대 연산 수만큼)
#
#     for i, op in enumerate(operations):
#         cmd, val = op.split()
#         val = int(val)
#
#         if cmd == 'I':
#             heapq.heappush(min_heap, (val, i))  # 값과 '고유 ID(인덱스)'를 같이 저장
#             heapq.heappush(max_heap, (-val, i))
#             visited[i] = True  # i번째로 들어온 값은 현재 유효하다.
#
#         elif cmd == 'D':
#             if val == 1:  # 최댓값 삭제
#                 # 이미 다른쪽에서 삭제된 '유령 데이터'들은 힙에서 털어냄
#                 while max_heap and not visited[max_heap[0][1]]:
#                     heapq.heappop(max_heap)
#
#                 if max_heap:
#                     visited[max_heap[0][1]] = False  # 진짜 삭제 처리 (방문 표시 해제)
#                     heapq.heappop(max_heap)
#             else:  # 최솟값 삭제
#                 # 이미 다른쪽에서 삭제된 '유령 데이터'들은 힙에서 털어냄
#                 while min_heap and not visited[min_heap[0][1]]:
#                     heapq.heappop(min_heap)
#
#                 if min_heap:
#                     visited[min_heap[0][1]] = False  # 진짜 삭제 처리
#                     heapq.heappop(min_heap)
#
#     # 모든 연산이 끝나고 남은 '유령 데이터' 한 번 더 정리
#     while max_heap and not visited[max_heap[0][1]]:
#         heapq.heappop(max_heap)
#     while min_heap and not visited[min_heap[0][1]]:
#         heapq.heappop(min_heap)
#
#     if not min_heap or not max_heap:
#         return [0, 0]
#     else:
#         return [-max_heap[0][0], min_heap[0][0]]


# Programmers

# from heapq import heap push, heappop

# def solution(arguments):
#     max_heap = []
#     min_heap = []
#     for arg in arguments:
#         if arg == "D 1":
#             if max_heap != []:
#                 heappop(max_heap)
#                 if max_heap == [] or -max_heap[0] < min_heap[0]:
#                     min_heap = []
#                     max_heap = []
#         elif arg == "D -1":
#             if min_heap != []:
#                 heappop(min_heap)
#                 if min_heap == [] or -max_heap[0] < min_heap[0]:
#                     max_heap = []
#                     min_heap = []
#         else:
#             num = int(arg[2:])
#             heappush(max_heap, -num)
#             heappush(min_heap, num)
#     if min_heap == []:
#         return [0, 0]
#     return [-heappop(max_heap), heappop(min_heap)]