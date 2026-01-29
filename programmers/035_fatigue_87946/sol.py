# GPT
def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n
    best = 0

    def dfs(left, cnt):
        nonlocal best
        if cnt > best:
            best = cnt

        for i, (minimum, minus) in enumerate(dungeons):
            if not visited[i] and left >= minimum:
                visited[i] = True
                dfs(left - minus, cnt + 1)
                visited[i] = False

    dfs(k, 0)
    return best

print(solution(80, [[80,20],[50,40],[30,10]]))  # 3


# GPT - Set
# def solution(k, dungeons):
#
#     def dfs(left, visited):
#         max_cnt = len(visited)  # 지금까지 돈 개수
#
#         for i, (minimum, minus) in enumerate(dungeons):
#             if i not in visited and left >= minimum:
#                 nxt = visited | {i}      # set 복사 + 추가
#                 cnt = dfs(left - minus, nxt)
#                 max_cnt = max(max_cnt, cnt)
#
#         return max_cnt  # ❗ 방문 집합이 아니라 "최대 개수" 반환
#
#
#     return dfs(k, set())
#
#
# print(solution(80, [[80,20],[50,40],[30,10]]))


# Programmers
solution = lambda k, d: max([solution(k - u, d[:i] + d[i+1:]) + 1 for i, (m, u) in enumerate(d) if k >= m] or [0])