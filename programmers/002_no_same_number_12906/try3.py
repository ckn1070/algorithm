# Solved - Done
def solution(arr):
    answer = []
    for a in arr:
        if not answer:
            answer.append(a)
            continue
        cur = answer[-1]
        if cur == a:
            continue
        else:
            answer.append(a)
    print(answer)
    return answer

solution([1,1,3,3,0,1,1])
solution([4,4,4,3,3])