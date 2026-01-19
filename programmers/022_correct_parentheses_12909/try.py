# Solved
def solution(s):
    key = {'(': 1, ')': -1}
    arr = []

    answer = True
    for i in s:
        if key[i] == 1:
            arr.append(i)
        else:
            if len(arr) == 0:
                answer = False
                break
            else:
                arr.pop()

    if len(arr) > 0:
        answer = False

    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('answer', answer)

    return answer

solution("()()")
solution("(())()")
solution(")()(")
solution("(()(")