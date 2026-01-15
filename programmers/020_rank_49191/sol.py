from collections import defaultdict, deque

# GPT
def solution(n, results):
    win = defaultdict(list)   # i -> i가 이긴 선수들
    lose = defaultdict(list)  # i -> i가 진 선수들(= i를 이긴 선수들)

    for a, b in results:
        win[a].append(b)
        lose[b].append(a)

    def bfs(start, graph):
        q = deque([start])
        visited = set([start])
        cnt = 0

        while q:
            cur = q.popleft()
            for nxt in graph[cur]:
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)
                    cnt += 1
        return cnt

    answer = 0
    for i in range(1, n + 1):
        down = bfs(i, win)    # i가 이길 수 있는 전체 수
        up = bfs(i, lose)     # i가 질 수 있는 전체 수
        if up + down == n - 1:
            answer += 1

    return answer


# Programmers
# def solution(n, results):
#     answer = 0
#     win, lose = defaultdict(set), defaultdict(set)
#     for result in results:
#             lose[result[1]].add(result[0])
#             win[result[0]].add(result[1])
#
#     for i in range(1, n + 1):
#         for winner in lose[i]: win[winner].update(win[i])
#         for loser in win[i]: lose[loser].update(lose[i])
#
#     for i in range(1, n+1):
#         if len(win[i]) + len(lose[i]) == n - 1: answer += 1
#     return answer