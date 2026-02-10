# Solved
def solution(brown, yellow):

    def outer(x, y):
        return (x+2)*(y+2)-x*y

    answer = []
    for i in range(yellow):
        ex = False
        for j in range(i+1):
            if j > i:
                break
            if (i+1)*(j+1) == yellow:
                if outer(i+1, j+1) == brown:
                    answer = [i+3, j+3]
                    ex = True
                    break
        if ex:
            break

    print(answer)
    return answer

solution(10, 2)
solution(8, 1)
solution(24, 24)