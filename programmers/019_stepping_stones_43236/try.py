# NOT Solved
def solution(distance, rocks, n):
    rocks.sort()

    dist = []
    for i in range(len(rocks)):
        if i == 0:
            dist.append(rocks[i])

        if i == len(rocks) - 1:
            dist.append(25 - rocks[i])
        else:
            dist.append(rocks[i+1]-rocks[i])
    dist.sort()

    print(dist)
    answer = 0
    return answer

solution(25, [2, 14, 11, 21, 17], 2)