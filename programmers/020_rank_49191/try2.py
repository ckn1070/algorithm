# NOT Solved
# 5/10 (시간초과)
# 내가봐도 구데기같이 풀기는 했다
#
# 우선 승과 패 그래프는 따로 만들어야 하는게 맞다
# 승으로 끝까지 간 그래프 + 패로 끝까지 간 그래프가 전체 모습과 같다면 순위를 매길 수 있다
#
# 그럼 BFS로 끝까지 가면 되겠네
# 선수 번호마다 달라져야 하니, 번호 i를 인풋
# 승과 패가 다르니, 그래프를 인풋
# 이긴 사람과 진 사람은 확실하게 다르니, 노드 수만 세면 되겠네
#
# Try 2
from collections import defaultdict, deque

def solution(n, results):
    win, lose = defaultdict(list), defaultdict(list)
    for w, l in results:
        win[w].append(l)
        lose[l].append(w)
    print('graph', win, lose)

    def dfs(i, graph):
        q = deque([i])
        visited = set([i])
        cnt = 0
        while q:
            cur = q.popleft()
            for j in graph[cur]:
                if j not in visited:
                    print('cur', cur, j)
                    q.append(j)
                    visited.add(j)
                    cnt += 1
        return cnt

    answer = 0
    for i in range(1, n+1):
        w = dfs(i, win)
        l = dfs(i, lose)
        print('res', i, w, l)
        if w + l == n - 1:
            answer += 1

    return answer


# Try 1
# from collections import defaultdict as dd, deque as dq
#
# def solution(n, results):
#     win = dd(list)
#     lose = dd(list)
#
#     for w, l in results:
#         win[w].append(l)
#         lose[l].append(w)
#     print('graph', win, lose)
#
#     answer = 0
#     for i in range(n):
#         win_v, lose_v, total = set(), set(), set()
#         win_q, lose_q = dq(win[i+1]), dq(lose[i+1])
#         total.add(i+1)
#         print('q', win_q, lose_q)
#
#         while win_q:
#             cur = win_q.popleft()
#             win_v.add(cur)
#             nxt = win[cur]
#             for j in nxt:
#                 if j not in win_v:
#                     win_q.append(j)
#         print('win', i, win_v)
#         while lose_q:
#             cur = lose_q.popleft()
#             lose_v.add(cur)
#             nxt = lose[cur]
#             for j in nxt:
#                 if j not in win_v:
#                     lose_q.append(j)
#         print('lose', i, lose_v)
#         total.update(win_v, lose_v)
#         print('total', total)
#         if len(total) == n: answer += 1
#
#     print('answer', answer)
#     return answer


# Programmers
# from collections import defaultdict
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

solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])