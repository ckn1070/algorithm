# Solved
def solution(array, commands):
    answer = []

    for i, j, k in commands:
        print('i, j, k', i, j, k )
        cur = sorted(array[i-1:j])
        answer.append(cur[k-1])

        print('ans', cur, answer)

    return answer

solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])


# Programmers
# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))