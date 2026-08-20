# Solved
def solution(arr):
    answer = []

    for i in arr:
        if len(answer) != 0:
            cur = answer.pop()
            answer.append(cur)
            print('cur: ', answer, cur, i)
            if i != cur:
                answer.append(i)
        else:
            answer.append(i)

    print('answer: ', answer)
    return answer

solution([1,1,3,3,0,1,1])
solution([4,4,4,3,3])


# Programmers
#
#
# def no_continuous(s):
#     # 함수를 완성하세요
#     a = []
#     for i in s:
#         if a[-1:] == [i]: continue
#         a.append(i)
#     return a