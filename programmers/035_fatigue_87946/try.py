# NOT Solved
# 반환값을 너무 잘못잡음
def solution(k, dungeons):

    arr = []
    def dfs(left, visited):
        for i, (minimum, minus) in enumerate(dungeons):
            print(i, minus, minimum, left)
            if i not in visited and left - minus >= 0 and left >= minimum:
                nxt = set(visited)
                nxt.add(i)
                cur = dfs(left - minus, nxt)
                arr.append(cur)
        return visited


    print(dfs(k, set()))
    print(arr)
    answer = -1
    return answer

solution(80, [[80,20],[50,40],[30,10]])