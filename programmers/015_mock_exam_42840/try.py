import collections
from collections import defaultdict


# Solved
def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    point = collections.defaultdict(int)

    for (idx, ans) in enumerate(answers):
        if first[idx % len(first)] == ans:
            point['1'] += 1
        if second[idx % len(second)] == ans:
            point['2'] += 1
        if third[idx % len(third)] == ans:
            point['3'] += 1

    sorted_items = sorted(point.items(), key=lambda x: x[1])

    answer = []
    win = sorted_items.pop()
    maximum = win[1]
    answer.append(int(win[0]))
    while sorted_items:
        cur = sorted_items.pop()
        if cur[1] == maximum:
            answer.append(int(cur[0]))
        else:
            break


    print(point)
    print(sorted(answer), maximum)
    return sorted(answer)

solution([1,2,3,4,5])
solution([1,3,2,4,2])