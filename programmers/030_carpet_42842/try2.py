# ? Solved
# 4/13 - ? 시간초과? - i++ 위치 잘못함;;
# 선 yellow 문제인줄알고 brown 먼저하도록 고치려다 코드 복잡해짐
# 깔끔하게 처음처럼 yellow 먼저해도됨;
def solution(brown, yellow):
    i = 3
    answer = []
    while i * i <= (brown + yellow):
        if (brown + yellow) % i == 0:
            fir, sec = i, (brown + yellow) // i
            print(fir, sec, brown, yellow)

            if (fir - 2) * (sec - 2) == yellow:
                answer = [max(fir, sec), min(fir, sec)]

        i += 1

    print('answer:', answer)
    return answer

solution(10, 2)
solution(8, 1)
solution(24, 24)