# Solved
#
# price 길이 100,000 - 많네
# 각 항목에 대해 전체를 훑는 방식은 n^2이라 안될듯
#
# price 각각이 자신보다 큰 값이 언제 나오는지 알아야하네
# 저번 스택/큐 문제에서 이런 비슷한 것을 했던 것 같은데..
# 어떻게 이렇게까지 하나도 기억이 안 날 수가 있지;;
# 반복문 2개 쓰는 느낌이었는데
#
# 와진짜 이걸 어케맞췄지; 사실 간신히 풀었음..
#
# Stack에는 오름차순으로 정렬해놓고, 빠지면 거꾸로 계속 빼면, 작은 것들만 남아있겠지
# Try 2
def solution(prices):
    n = len(prices)
    st = []
    answer = [0] * n
    for i, p in enumerate(prices):
        while st:
            idx, price = st.pop()
            if price > p:
                answer[idx] = i - idx
            else:
                st.append((idx, price))
                break
        st.append((i, p))

    while st:
        idx, price = st.pop()
        answer[idx]= n - 1 - idx

    print(answer)
    return answer


# Try 1
# import heapq
#
# def solution(prices):
#     n = len(prices)
#     answer = [0] * n
#
#     q = []
#     t = 0
#     for i, p in enumerate(prices):
#         t += 1
#         while q:
#             np, nt = heapq.heappop(q)
#             if np > p:
#                 answer[nt] = t - nt
#             else:
#                 heapq.heappush(q, (np, nt))
#                 break
#         heapq.heappush(q, (-p, i + 1))
#
#     # while q:
#     #     np, nt = heapq.heappop(q)
#     #     answer[nt] = t - nt
#
#     print(answer)
#     return answer

solution([1, 2, 3, 2, 3])