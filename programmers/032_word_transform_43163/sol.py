# Programmers
from collections import deque

def get_adjacent(current, words):
    for word in words:
        if len(current) != len(word):
            continue

        count = 0
        for c, w in zip(current, word):
            if c != w:
                count += 1

        if count == 1:
            yield word


def solution(begin, target, words):
    dist = {begin: 0}
    queue = deque([begin])

    while queue:
        current = queue.popleft()

        for next_word in get_adjacent(current, words):
            if next_word not in dist:
                dist[next_word] = dist[current] + 1
                queue.append(next_word)

    return dist.get(target, 0)

from collections import deque


# GPT
# def solution(begin, target, words):
#     if target not in words:
#         return 0
#
#     def can_go(a, b):
#         diff = 0
#         for x, y in zip(a, b):
#             if x != y:
#                 diff += 1
#                 if diff > 1:
#                     return False
#         return diff == 1
#
#     q = deque([(begin, 0)])
#     visited = set([begin])
#
#     while q:
#         cur, d = q.popleft()
#         for w in words:
#             if w not in visited and can_go(cur, w):
#                 if w == target:
#                     return d + 1
#                 visited.add(w)
#                 q.append((w, d + 1))
#     return 0
