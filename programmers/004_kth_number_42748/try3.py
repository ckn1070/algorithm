# Solved - Done
def solution(array, commands):
    answer = []
    for i, j, k in commands:
        sub = sorted(array[i - 1:j])
        answer.append(sub[k-1])
    print(answer)
    return answer

solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])