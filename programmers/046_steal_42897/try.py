# NOT Solved
# Greedy로 접근했다가 조건도 꼬이고 시간 초과..
from collections import deque

def solution(money):
    # visited = [False]*len(money)
    iv, ii = max(money), money.index(max(money))
    q = deque([(iv, ii)])

    answer = 0
    while q:
        cur, idx = q.popleft()
        print('answer', cur)
        answer += cur
        money[idx] = -1
        if idx == 0:
            money[len(money)-1] = -1
        else:
            money[idx-1] = -1

        if idx == len(money) - 1:
            money[0] = -1
        else:
            money[idx+1] = -1

        nv, ni = max(money), money.index(max(money))
        if nv != -1:
            q.append((nv, ni))


    print(answer)
    return answer

solution([1, 2, 3, 1])