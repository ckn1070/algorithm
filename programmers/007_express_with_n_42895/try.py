# NOT Solved
def solution(N, number):
    res = []
    def rec(cur, count):
        if count >= 8:
            print('-1: ', cur)
            res.append(-1)
            return
        if eval(cur) == number:
            print('res: ', count, '; ', cur)
            res.append(count)
            return

        count += 1
        n = str(N)
        rec(cur + n, count)
        rec(cur + '+' + n, count)
        rec(cur + '-' + n, count)
        rec(cur + '*' + n, count)
        rec(cur + '/' + n, count)

    answer = 0
    rec(str(N), 1)
    # print(res)
    return answer

solution(5, 12)
# solution(2, 11)
