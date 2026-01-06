# Programmers
def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)

# GPT
# def solution(n, lost, reserve):
#     lost_set = set(lost) - set(reserve)
#     reserve_set = set(reserve) - set(lost)
#
#     for r in sorted(reserve_set):
#         if r-1 in lost_set:
#             lost_set.remove(r-1)
#         elif r+1 in lost_set:
#             lost_set.remove(r+1)
#
#     return n - len(lost_set)

solution(5, [2, 4], [1, 3, 5])
solution(5, [2, 4], [3])
solution(3, [3], [1])