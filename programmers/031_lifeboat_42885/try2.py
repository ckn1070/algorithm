#
# 22/22, 0/5 - 뭐지 이 비효율의 끝판왕은;;
# 22/22, 3/5 - pop(0)으로도 2개는 틀리네;
# 큐까지 써서 간신히 통과;
# Try 3
from collections import deque

def solution(people, limit):
    people.sort(reverse=True)
    q = deque(people)
    print(q, q[2])

    answer = 0
    while q:
        big = q.popleft()
        if q and big + q[-1] <= limit:
            q.pop()
        answer += 1

    print(answer)
    return answer



# Try 2
# def solution(people, limit):
#     people.sort()
#
#     answer = 0
#     while people:
#         big = people.pop()
#         if people and big + people[0] <= limit:
#             people.pop(0)
#         answer += 1
#
#     print(answer)
#     return answer


# Try 1
# def solution(people, limit):
#     people.sort(reverse=True)
#
#     answer = 0
#     while people:
#         small = people.pop()
#         for i in range(len(people)):
#             if people[i] + small <= 100:
#                 people.pop(i)
#                 break
#         answer += 1
#
#     print(answer)
#     return answer

solution([70, 50, 80, 50], 100)
solution([70, 80, 50], 100)
solution([70, 50, 80, 50, 30, 20, 90], 100)
