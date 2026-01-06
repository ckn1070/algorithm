# Solved
def solution(array, commands):
    answer = []

    for arr in commands:
        tmp = array[arr[0] - 1 : arr[1]]
        tmp.sort()
        res = tmp[arr[2] - 1]
        answer.append(res)

    print(answer)
    return answer

solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]])