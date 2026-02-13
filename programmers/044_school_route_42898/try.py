# NOT Solved
# DP 개념 아직도 잘 안 와닿음..
# 기존 경로 누적
from collections import deque, defaultdict

def solution(m, n, puddles):
    total = 0
    q = deque((1, 1, 0))
    before = defaultdict(int)
    after = defaultdict(int)

    while q:
        x, y, d = q.pop()
        if (x+1 == m and y == n) or (x == m and y+1 == n):
            total += 1
        # else:
        #     if []

    answer = 0
    return answer

solution(4, 3, [[2, 2]])