# NOT Solved
# 딱 하나 시간초과..
from collections import defaultdict as dd
from itertools import combinations

def solution(clothes):
    kind = dd(int)

    for i, j in clothes:
        kind[j] += 1

    keys = list(kind.keys())
    answer = 0
    for k in range(len(keys)):
        com = combinations(keys, k+1)
        for l in com:
            cnt = 1
            for m in l:
                cnt *= kind[m]
            answer+=cnt

    print(answer)

    return answer

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])