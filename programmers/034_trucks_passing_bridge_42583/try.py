# NOT Solved
# 초 계산이 어떻게 되는건지 모르겠네..
# 배치 방식이라 운 좋으면 맞고, 아니면 틀리고..
# 한 대씩 계산해야한다는 건 알긴 알겠는데..
from collections import deque

def solution(bridge_length, weight, truck_weights):
    q = deque(truck_weights)
    passing = []
    bridge = 0

    while q:
        cur = q.popleft()
        print('cur: ', cur, bridge, passing)
        if sum(passing) + cur > weight or len(passing) >= bridge_length:
            bridge += bridge_length
            if len(passing) == bridge_length:
                bridge += 1
            print('cur: ', cur, bridge)
            passing = []

        passing.append(cur)

    if passing:
        bridge += len(passing) + bridge_length

    print(bridge)
    answer = 0
    return answer

solution(2, 10, [7,4,5,6])
# solution(100, 100, [10])
# solution(100, 100, [10,10,10,10,10,10,10,10,10,10])