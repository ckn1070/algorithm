import heapq

# GPT
def solution(jobs):
    n = len(jobs)

    # (요청시각 s, 소요시간 l, 작업번호 i)
    jobs_sorted = sorted((s, l, i) for i, (s, l) in enumerate(jobs))

    heap = []   # (소요시간 l, 요청시각 s, 작업번호 i)
    t = 0
    idx = 0
    total = 0

    while idx < n or heap:
        # 현재 시각까지 도착한 작업들을 heap에 넣기
        while idx < n and jobs_sorted[idx][0] <= t:
            s, l, i = jobs_sorted[idx]
            heapq.heappush(heap, (l, s, i))
            idx += 1

        if heap:
            l, s, i = heapq.heappop(heap)
            t += l
            total += (t - s)
        else:
            # heap이 비었으면 다음 작업 요청 시각으로 점프 (idx<n 보장 필요)
            if idx < n:
                t = jobs_sorted[idx][0]

    return total // n

# Programmers
# import heapq
# from collections import deque
#
# def solution(jobs):
#     tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
#     q = []
#     heapq.heappush(q, tasks.popleft())
#     current_time, total_response_time = 0, 0
#     while len(q) > 0:
#         dur, arr = heapq.heappop(q)
#         current_time = max(current_time + dur, arr + dur)
#         total_response_time += current_time - arr
#         while len(tasks) > 0 and tasks[0][1] <= current_time:
#             heapq.heappush(q, tasks.popleft())
#         if len(tasks) > 0 and len(q) == 0:
#             heapq.heappush(q, tasks.popleft())
#     return total_response_time // len(jobs)