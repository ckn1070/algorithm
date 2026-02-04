# NOT Solved
# 감도 못잡음..
def solution(routes):
    routes.sort()
    print(routes)
    answer = 0

    left, right, meet = routes[0][0], routes[0][1], False
    for i, (l, r) in enumerate(routes):
        if i == 0: continue
        nxt = meet
        print(left, right, meet, l, r, right < l)
        if left < l and right > r:
            print('1', l, r)
            left, right, nxt = l, r, True
        elif l <= right <= r:
            print('2', l, r)
            nxt = True
        elif right < l:
            print('4', l, r)
            answer += 1
            left, right, nxt = l, r, False

        if not nxt and meet: answer += 1
        meet = nxt

    print(answer)
    return answer

from collections import deque
# def solution(routes):
#     routes.sort()
#     print(routes)
#     answer = 0
#
#     return answer

solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])