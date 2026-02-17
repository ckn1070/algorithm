# NOT Solved
# 이미 연산한 값을 저장하고 있을 필요..
def solution(arr):

    ans = []
    def rec(array):
        for i in range(int((len(array)-1)/2)):
            left, center, right = array[:2*i], array[2*i:2*i+3], array[2*i+3:]
            print(eval(''.join(center)))
            print(left, center, right)
            nxt = left + [str(eval(''.join(center)))] + right
            if len(nxt) == 1:
                ans.append(nxt[0])
            else:
                rec(nxt)

    rec(arr)
    print('ans', ans)
    ans.sort()
    answer = int(ans[-1])
    return answer

solution(["1", "-", "3", "+", "5", "-", "8"])
solution(["5", "-", "3", "+", "1", "+", "2", "-", "4"])