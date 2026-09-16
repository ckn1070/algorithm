# Solved (Strange)
#
# 우선순위: 작업 소요시간 짧음 > 작업 요청 시각 빠름 > 작업 번호 작음
# Jobs - Idx: 작업 번호, [s: 요청 시점, l: 소요시간]
import heapq

def solution(jobs):
    jobs_sorted = sorted(((l, s, i) for i, (s, l) in enumerate(jobs)), key=lambda x: (x[1], x[0], x[2]))

    q = []
    idx, t, times, n = 0, 0, 0, len(jobs_sorted)
    print(jobs_sorted)

    while idx < n or q:
        while idx < n and jobs_sorted[idx][1] <= t:
            heapq.heappush(q, jobs_sorted[idx])
            idx += 1

        if q:
            cur = heapq.heappop(q)
            t += cur[0]
            times += t - cur[1]
            print('times', times, cur)
        else:
            if idx < n:
                t = jobs_sorted[idx][1]

    answer = times // len(jobs)
    print('answer:', answer)

    return answer


# 후보가 계속 들어오고, 후보 중 최솟값/최댓값을 계속 꺼내야 하면 Heap을 떠올리기
#
# 음..? Heap 문제인데 Heap을 쓰지 않고 풀어버렸다
#
# Try 2 - 10/20 -> 정답;
# 아무리 봐도 너무 구질구질한데, 심지어 반은 틀림
# 우선순위대로 정렬하는 것까진 알겠는데, 먼저 들어온 요청이랑 어떻게 같이 처리하지
# def solution(jobs):
#     q = []
#     times = []
#
#     for i, (s, l) in enumerate(jobs):
#         q.append([l, s, i])
#     q.sort(key=lambda x: x[1], reverse=True)
#     print('q', q)
#
#     t = 0
#     jq = [q.pop()]
#     while jq:
#         while q and q[-1][1] <= t:
#             jq.append(q.pop())
#             jq.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)
#         print(t, jq)
#         cur = jq.pop()
#         if cur[1] <= t:
#             t += cur[0]
#             times.append(t - cur[1])
#             # 처음에 jq가 비어있지 않아도 무작정 넣어서 틀렸다
#             if q and not jq:
#                 nxt = q.pop()
#                 if nxt[1] > t:
#                     t = nxt[1]
#                 jq.append(nxt)
#         else:
#             t += 1
#             jq.append(cur)
#
#     print('times', times)
#
#     cnt = 0
#     for j in times:
#         cnt += j
#
#     answer = cnt // len(times)
#     print('answer', answer)
#     return answer


# Try 1
# def solution(jobs):
#     q = []
#     times = []
#
#     for i, (s, l) in enumerate(jobs):
#         q.append([l, s, i])
#     q.sort(key=lambda x: (x[0], x[1], x[2]), reverse=True)
#     print('q', q)
#
#     t = 0
#     while q:
#         cur = q.pop()
#         if cur[1] <= t:
#             t += cur[0]
#             times.append(t - cur[1])
#         else:
#             t += 1
#             q.append(cur)
#
#     print('times', times)
#
#     cnt = 0
#     for j in times:
#         cnt += j
#
#     answer = cnt // len(times)
#     print('answer', answer)
#     return answer


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


solution([[0, 3], [1, 9], [3, 5]])