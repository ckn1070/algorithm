# Solved
def solution(s):
    answer = True
    opened = 0

    for c in s:
        if c == '(':
            opened += 1
        else:
            if opened > 0:
                opened -= 1
            else:
                answer = False
                break
    if opened != 0:
        answer = False

    print(s, opened, answer)
    return answer

solution("()()")
solution("(())()")
solution(")()(")
solution("(()(")