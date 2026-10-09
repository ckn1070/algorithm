# Solved
# BFS로 풀면 결과가 나오는 순간 최솟값이 되겠구나
def solution(begin, target, words):
    visited = []
    n = len(target)
    total = set()

    def dfs(current, ts):
        for w in words:
            if w in visited:
                continue

            cnt = 0
            for i in range(n):
                if w[i] == current[i]:
                    cnt += 1

            print('count', current, w, cnt)
            if cnt == n-1:
                if w == target:
                    total.add(ts)

                visited.append(current)
                dfs(w, ts + 1)
                visited.remove(current)

    dfs(begin, 1)
    answer = min(total) if total else 0
    print(total, answer)
    return answer

solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"])
solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"])