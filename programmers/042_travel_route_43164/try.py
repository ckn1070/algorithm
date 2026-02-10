# NOT Solved
# 간선 파괴로 못 되돌아옴..
from collections import defaultdict

def solution(tickets):
    routes = defaultdict(list)

    for s, e in tickets:
        routes[s].append(e)
    for k in routes:
        routes[k].sort(reverse=True)
    print(routes)

    arr = []
    def dfs(cur, visited):
        cand = routes[cur]
        if not cand or len(set(visited)) == len(routes.keys()):
            arr.append(visited)
        for nxt in cand:
            nv = visited[:]
            nv.append(nxt)
            dfs(nxt, nv)

    # def dfs(cur, visited):
    #     if not routes[cur]: return
    #     nxt = routes[cur].pop()
    #     print(cur, nxt, visited)
    #     visited.append(nxt)
    #     dfs(nxt, visited)


    answer = ["ICN"]
    dfs("ICN", answer)
    print(answer)
    print('arr', arr)

    return answer

solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])