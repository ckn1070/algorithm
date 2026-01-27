# GPT
from collections import deque

def solution(people, limit):
    q = deque(sorted(people))
    boats = 0

    while q:
        heaviest = q.pop()          # 가장 무거운 사람은 일단 태움
        if q and heaviest + q[0] <= limit:
            q.popleft()             # 가장 가벼운 사람과 같이 태울 수 있으면 같이
        boats += 1

    return boats

# GPT - Two Pointer
# def solution(people, limit):
#     people.sort()
#     i, j = 0, len(people) - 1
#     boats = 0
#
#     while i <= j:
#         if people[i] + people[j] <= limit:
#             i += 1
#         j -= 1
#         boats += 1
#
#     return boats

# Programmers
# def solution(people, limit) :
#     answer = 0
#     people.sort()
#
#     a = 0
#     b = len(people) - 1
#     while a < b :
#         if people[b] + people[a] <= limit :
#             a += 1
#             answer += 1
#         b -= 1
#     return len(people) - answer