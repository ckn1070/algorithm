# Solved - Done
def solution(sizes):
    width = 0
    height = 0
    for x, y in sizes:
        w = max(x, y)
        h = min(x, y)
        width = max(w, width)
        height = max(h, height)

    answer = width * height
    print(answer)
    return answer

solution([[60, 50], [30, 70], [60, 30], [80, 40]])
solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])
solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])