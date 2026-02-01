# Programmers
def solution(n, wires):
    ans = n
    for sub in (wires[i+1:] + wires[:i] for i in range(len(wires))):
        s = set(sub[0])
        [s.update(v) for _ in sub for v in sub if set(v) & s]
        ans = min(ans, abs(2 * len(s) - n))
    return ans

# GPT
# from collections import defaultdict, deque
#
# def solution(n, wires):
#     tree = defaultdict(list)
#     for a, b in wires:
#         tree[a].append(b)
#         tree[b].append(a)
#
#     def bfs(start, cut_a, cut_b):
#         visited = set([start])
#         q = deque([start])
#
#         while q:
#             cur = q.popleft()
#             for nxt in tree[cur]:
#                 # 끊은 간선 (cut_a - cut_b) 무시 (양방향)
#                 if (cur == cut_a and nxt == cut_b) or (cur == cut_b and nxt == cut_a):
#                     continue
#                 if nxt not in visited:
#                     visited.add(nxt)
#                     q.append(nxt)
#
#         return len(visited)
#
#     answer = n  # 최댓값은 n-2이지만 대충 n으로 시작
#     for a, b in wires:
#         left = bfs(a, a, b)
#         right = n - left
#         answer = min(answer, abs(left - right))
#
#     return answer
