# NOT Solved
# 다리 위에 트럭 bridge_length 대
# 다리가 견딜 수 있는 무게 weight
# 트럭별 무게 truck_weights
#
# 이게 대체 어떻게 2점짜리지..
# 저번에도 굉장히 까다로웠던 것으로 기억..
#
# time 계산하는것, weight 계산하는 것까진 맞았는데
# while 제대로 못썼고, bridge를 제대로 못썼네
#
# Bridge 자체를 Queue로 만들 수가 있겠구나
# 그럼 한 번에 1초씩만 생각할 수가 있겠구나
from collections import deque

# Try 3
def solution(bridge_length, weight, truck_weights):
    bridge = deque([0] * bridge_length)
    trucks = deque(truck_weights)
    t, bw = 0, 0

    while trucks or bw > 0:
        t += 1
        nxt = bridge.popleft()
        bw -= nxt

        if trucks:
            truck = trucks.popleft()
            if bw + truck <= weight:
                bw += truck
                bridge.append(truck)
            else:
                trucks.appendleft(truck)
                bridge.append(0)

    answer = 0
    print(t)
    return answer


# Try 2
# def solution(bridge_length, weight, truck_weights):
#     trucks = deque(truck_weights)
#     init = trucks.popleft()
#     q = deque([(init, 1)])
#     t = 1
#     sum_weight = init
#
#     while q:
#         while trucks:
#             nxt = trucks.popleft()
#             if sum_weight + nxt <= weight:
#                 sum_weight += nxt
#                 t += 1
#                 q.append((nxt, t))
#             else:
#                 break
#         tr, ti = q.popleft()
#         if ti - t < bridge_length:
#             t = ti
#         sum_weight -= tr
#
#         if not q and trucks:
#             nxt = trucks.popleft()
#             sum_weight += nxt
#             q.append((nxt, t))
#
#     print(t)
#     answer = 0
#     return answer


# Try 1
# def solution(bridge_length, weight, truck_weights):
#     q = deque()
#
#     t = 0
#     sum_weight = 0
#     for truck in truck_weights:
#         sum_len = 0
#
#         while q:
#             w, i = q.popleft()
#             sum_len += 1
#             sum_weight += w
#             if i + 1 < bridge_length:
#                 q.append((w, i + 1))
#             t += 1
#
#         if sum_len + 1 <= bridge_length and sum_weight + truck <= weight:
#             q.append((truck, 1))
#
#     print(t)
#     answer = 0
#     return answer

solution(2, 10, [7,4,5,6])
solution(100, 100, [10])
solution(100, 100, [10,10,10,10,10,10,10,10,10,10])