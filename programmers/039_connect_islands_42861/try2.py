# NOT Solved
# DFS로 전부 탐색하기엔 섬의 개수가 너무 많은데
# BFS라기엔 시작점이 없는데..
# DP인가; 이게 DP로 되나;
#
# 엥 근데 읽다보니 내가 쓴 코드가 느낌은 비슷한데..?;;
# 아 사이클이 있는 것을 검사를 안했구나..
# GPT 피셜 Prim이랑 더 비슷하다는데
#
# Kruskal: 최소 신장 트리 (간선 가중치의 합이 최소)
# Union - Find (Disjoint Set)
#
# parent가 대표 (root)를 정하는거라고 보면 된다
# 처음에 각자가 대표 (전부 서로소)
# 그러다 union > else에서 최초로 parent에 소속되고, rank 기준으로 parent (root)를 정하게 된다
# 그래서 사실 rank 없어도 되네;
# 그러나 parent가 같으면 false를 반환 (사이클을 만들기 때문에)
# union에서 사용하는 find가 parent를 찾는 직접적인 함수
# find는 parent를 찾으면서 direct로 적히도록 바꾸는 역할도 동시 수행
# 2/8
# Try 2
def solution(n, costs):
    parent = [i for i in range(n)]
    print(parent)
    rank = [0] * n

    def find(x):
        while parent[x] != x:
            # print('par', x, parent[x], parent[parent[x]])
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        fa, fb = find(a), find(b)
        print(a, b, fa, fb)
        if fa == fb:
            return False

        if rank[fa] < rank[fb]:
            parent[fa] = fb
            rank[fb] += 1
        elif rank[fa] > rank[fb]:
            parent[fb] = fa
            rank[fa] += 1
        else:
            parent[fb] = fa
            rank[fa] += 1
        return True

    costs.sort(key=lambda x: x[2])

    answer = 0
    edge = 0
    for i, j, c in costs:
        if union(i, j):
            answer += c
            edge += 1
            print('union', i, j, answer)
        if edge == n - 1:
            break

    print(answer)
    return answer


# Try 1
# def solution(n, costs):
#     total = []
#     for x, y, c in costs:
#         total.append([x, y, c])
#         total.append([y, x, c])
#     total.sort(key=lambda x: (x[2], x[0], [1]))
#     print(total)
#
#     visited = set()
#     answer = 0
#     for s, e, co in total:
#         if len(visited) == n:
#             break
#         if s not in visited and e not in visited:
#             visited.add(s)
#             visited.add(e)
#             answer += co
#         elif e not in visited:
#             visited.add(e)
#             answer += co
#
#     print(answer)
#     return answer

solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])