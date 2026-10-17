# Solved
# 경우의 수가 6^5인데 전체 다 해보는게 말이 되나.. 라고 했는데 7천개 정도밖에 안되네;
# 아니네? 3905개네? 5^5+5^4...5 / 아 6^5는 안되겠구나 중간에 ''가 있는 조합은 안되는구나 없어져버리지
# DFS?
def solution(word):
    visited = []
    def dfs(cur, visited):
        cand = ['A', 'E', 'I', 'O', 'U']

        for ch in cand:
            nxt = cur + ch
            if len(nxt) <= 5 and nxt not in visited:
                visited.append(nxt)
                dfs(nxt, visited)
    dfs('', visited)
    print(len(visited), visited.index(word), visited)
    answer = visited.index(word)+1
    return answer

solution("AAAAE")
solution("AAAE")
solution("I")
solution("EIO")