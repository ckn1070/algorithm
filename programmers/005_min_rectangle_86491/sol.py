# GPT
def solution(sizes):
    max_w = 0  # 긴 변들 중 최댓값
    max_h = 0  # 짧은 변들 중 최댓값

    for w, h in sizes:
        long_side = max(w, h)
        short_side = min(w, h)

        max_w = max(max_w, long_side)
        max_h = max(max_h, short_side)

    answer = max_w * max_h
    print(answer)
    return answer

# Programmers
# def solution(sizes):
#     return max(max(x) for x in sizes) * max(min(x) for x in sizes)

solution([[60, 50], [30, 70], [60, 30], [80, 40]])
solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])
solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])