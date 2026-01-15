from collections import defaultdict as dd

# NOT Solved
# 첫 접근은 맞았으나.. 그 이후로 감을 잡지 못함...
def solution(n, results):
    win = dd(list)
    lose = dd(list)

    for i, j in results:
        win[i].append(j)
        lose[j].append(i)

    print(win)
    print(lose)
    answer = 0
    return answer

solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])