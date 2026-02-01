# Solved
def solution(prices):
    time = [0] * len(prices)
    stack = []

    for i, v in enumerate(prices):
        if not stack:
            stack.append((v, i))
            continue
        while stack and stack[-1][0] > v:
            maximum = stack.pop()
            time[maximum[1]] = i-maximum[1]
        stack.append((v, i))

    print(time, stack)
    maximum = stack.pop()
    for v, i in stack:
        time[i] = maximum[1] - i
    print(time, stack)

    return time

solution([1, 2, 3, 2, 3])