# Solved
from collections import defaultdict

def solution(n, lost, reserve):
    counter = defaultdict(int)

    for i in range(n):
        c = i+1
        counter[c] = 1
        if c in reserve:
            counter[c] += 1
        if c in lost:
            counter[c] -= 1

    for k in [k for k in counter.keys()]:
        if k > 1:
            if counter[k-1] == 0 and counter[k] > 1:
                counter[k-1] += 1
                counter[k] -= 1
        if k < n:
            if counter[k + 1] == 0 and counter[k] > 1:
                counter[k + 1] += 1
                counter[k] -= 1

    answer = sum(1 for v in counter.values() if v >= 1)
    print(counter)
    print(answer)
    return answer

solution(5, [2, 4], [1, 3, 5])
solution(5, [2, 4], [3])
solution(3, [3], [1])