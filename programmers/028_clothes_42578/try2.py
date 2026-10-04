# NOT Solved
#
# Combination을 써야할 것 같아서, DFS까지 했는데
# DFS 자체를 구현을 못했다 미친
#
# 이건 그냥 수학 문제 같은데;;
# 어차피 모든 것들을 독립적으로 조합하는 경우의 수를 구할 건데,
# 각 종류별로 안입는 경우를 상정해서 1가지를 더 키워서 계산하면 된다
# Try 2
from collections import defaultdict

def solution(clothes):
    c_set = defaultdict(int)

    for _, k in clothes:
        c_set[k] += 1

    answer = 1
    for key in c_set.keys():
        answer *= (c_set[key] + 1)

    print(answer)
    return answer -1


# Try 1
# from collections import defaultdict
#
# def solution(clothes):
#     c_set = defaultdict(int)
#
#     for n, k in clothes:
#         c_set[k] += 1
#     keys = list(c_set.keys())
#
#     total = set()
#     visited = [False] * len(keys)
#     def dfs(comb, idx):
#         print(idx, comb)
#         for i in range(len(keys)):
#             if not visited[i]:
#                 visited[i] = True
#                 comb.append(keys[idx])
#                 total.add(comb)
#                 if i+1 < len(keys):
#                     dfs(comb, i)
#                     visited[i] = False
#                     comb.pop()
#     dfs([], 0)
#
#     print(c_set, total)
#
#     answer = 0
#     return answer

solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])
solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])