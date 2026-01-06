# Solved
def solution(numbers, target):

    res = []
    def bfs(n, arr):
        if len(arr) > 0:
            new = arr[1:]
            # print(n, arr)
            bfs(n + arr[0], new)
            bfs(n - arr[0], new)

        else:
            res.append(n)

    bfs(0, numbers)
    answer = res.count(target)
    print('answer', answer)
    return answer

solution([1, 1, 1, 1, 1], 3)
solution([4, 1, 2, 1], 4)