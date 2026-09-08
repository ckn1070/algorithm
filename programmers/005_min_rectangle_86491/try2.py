# Solved
# 풀긴 했는데 진짜 간신히 풀었달까..
# 이 간단한게 왜이렇게 어려웠지..?
# 가로랑 세로랑 논리가 같아야 하는건데;;
def solution(sizes):
    minimum = 0
    maximum = 0

    for m, n in sizes:
        print('', minimum, maximum)
        w = max(m, n)
        h = min(n, m)

        if w > maximum:
            maximum = w
        if h > minimum:
            minimum = h

    print('size', maximum, minimum)

    answer = maximum * minimum
    return answer

solution([[60, 50], [30, 70], [60, 30], [80, 40]])
solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])
solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])


# Programmers
# def solution(sizes):
#     return max(max(x) for x in sizes) * max(min(x) for x in sizes)
