# NOT Solved
# 런타임 에러.. (시간초과)
def solution(triangle):

    res = []
    def rec(sub, index, current):
        print('cur: ', index, current, sub, len(sub), res)
        if len(sub) > 1:
            print(index+index, current, sub[0][index])
            rec(sub[1:],index+0,  current+sub[0][index])
            rec(sub[1:],index+1,  current+sub[0][index+1])
        else:
            res.append(current+sub[0][index])
            res.append(current + sub[0][index+1])

    rec(triangle[1:], 0, 0)
    print(res)

    answer = max(res) + triangle[0][0]
    print('asw: ', answer)
    return answer

solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])