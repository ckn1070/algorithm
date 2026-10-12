# Solved
# 던전: 최소 피로도, 소모 피로도 (최소 >= 소모) - 같은 던전 여러개 가능 (1 ~ 8개)
# k: 현재 피로도
#
# 던전이 8개밖에 없고, 최댓값이니, DFS를 써야하나
def solution(k, dungeons):
    visited = set()
    expcnt = set()

    def dfs(cur, cnt):
        for i, (need, lose) in enumerate(dungeons):
            if i not in visited and cur >= need:
                visited.add(i)
                expcnt.add(cnt + 1)
                dfs(cur - lose, cnt + 1)
                visited.remove(i)

    dfs(k, 0)
    print(expcnt)
    answer = max(expcnt)
    return answer

solution(80, [[80,20],[50,40],[30,10]])