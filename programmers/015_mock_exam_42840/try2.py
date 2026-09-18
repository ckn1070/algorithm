def solution(answers):
    maximum = 10_000
    first = [1, 2, 3, 4, 5] * ((maximum // 5) + 1)
    second = [2, 1, 2, 3, 2, 4, 2, 5] * ((maximum // 8) + 1)
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * ((maximum // 10) + 1)

    correct = [[0, 1], [0, 2], [0, 3]]
    for i, ans in enumerate(answers):
        if ans == first[i]:
            correct[0][0] += 1
        if ans == second[i]:
            correct[1][0] += 1
        if ans == third[i]:
            correct[2][0] += 1

    answer = []
    correct.sort(reverse=True)
    top = 0
    for c, p in correct:
        if c >= top:
            top = c
            answer.append(p)

    answer.sort()
    print('answer', answer)
    return answer


solution([1,2,3,4,5])
solution([1,3,2,4,2])


# Programmers
# def solution(answers):
#     pattern1 = [1,2,3,4,5]
#     pattern2 = [2,1,2,3,2,4,2,5]
#     pattern3 = [3,3,1,1,2,2,4,4,5,5]
#     score = [0, 0, 0]
#     result = []
#
#     for idx, answer in enumerate(answers):
#         if answer == pattern1[idx%len(pattern1)]:
#             score[0] += 1
#         if answer == pattern2[idx%len(pattern2)]:
#             score[1] += 1
#         if answer == pattern3[idx%len(pattern3)]:
#             score[2] += 1
#
#     for idx, s in enumerate(score):
#         if s == max(score):
#             result.append(idx+1)
#
#     return result