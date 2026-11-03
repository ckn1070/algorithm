# Solved - 아직도 DFS는 불안불안..
# DFS 시도했다가 BFS로 풀었다
#
# 두 개로 퍼져나갈 때 set은 하나로 쓰면 안될듯?
#
# 아예 input 자체를 바꿔버려도 된다는 것 생각하기 - 그러면 input으로 끝을 알 수 있다
#
# Try 3 - DFS
def solution(numbers, target):
    answer = 0
    def dfs(nums, ip):
        nonlocal answer
        if len(nums) == 0:
            if ip == target:
                answer += 1
        else:
            dfs(nums[1:], ip - nums[0])
            dfs(nums[1:], ip + nums[0])

    dfs(numbers, 0)
    print(answer)
    return answer


# Try 2 - BFS Solved
# from collections import deque
#
# def solution(numbers, target):
#     init = numbers[0]
#     q = deque([(init, 0), (-init, 0)])
#     n = len(numbers)
#
#     answer = 0
#     while q:
#         cur, idx = q.popleft()
#         print(cur, idx)
#         if idx == n - 1:
#             if cur == target:
#                 answer += 1
#         else:
#             nxt = numbers[idx + 1]
#             q.append((cur + nxt, idx + 1))
#             q.append((cur - nxt, idx + 1))
#     print(answer)
#     return answer

# Try 1 - DFS NOT Solved
# def solution(numbers, target):
#     visited = [False] * len(numbers)
#
#     answer = 0
#     def rec(ip):
#         nonlocal answer
#         if ip == target and False not in visited:
#             answer += 1
#         for i, num in enumerate(numbers):
#             if not visited[i]:
#                 visited[i] = True
#                 # print(i, ip, num)
#                 rec(ip + num)
#                 rec(ip - num)
#                 visited[i] = False
#
#     rec(0)
#     print(answer)
#     return answer

solution([1, 1, 1, 1, 1], 3)
solution([4, 1, 2, 1], 4)