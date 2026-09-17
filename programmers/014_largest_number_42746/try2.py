# NOT Solved
#
# Sort 자체의 사용 방식을 좀 알아야하네
#
# 내가 Try 1에서 시도했던 방식은, 내가 직접 Sort를 만드는 것이었는데,
# 이건 너무 비효율적이어서 시간 초과가 나올 수밖에 없다
#
# 0이 되는 경우도 신경을 써주어야 한다
#
# 1차: 실패
# - 아예 오답
# - 한 번 순서를 바꿔서 안되는 경우가 있을 수 있다
# 2차: 실패
# - 5/15 시간초과, 1/15 오답
# 역시 전체 for문을 계속 다시 돌리는 데에는 문제가 있을 수밖에..
# Try 2
from functools import cmp_to_key

def solution(numbers):

    def cmp(a, b):
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        else:
            return 0

    str_num = [str(i) for i in numbers]
    str_num.sort(key=cmp_to_key(cmp))

    answer = ''.join(str_num)
    print('answer', answer)
    return '0' if str_num[0] == '0' else answer


# Try 1
# def solution(numbers):
#     str_num = [str(i) for i in numbers]
#     str_num.sort(reverse=True)
#     print(str_num)
#
#     answer = ''
#     cur = len(str_num)-1
#     while cur > 0:
#         cur = len(str_num) - 1
#         for i in range(len(str_num)-1):
#             if str_num[i][0] == str_num[i+1][0] and int(str_num[i] + str_num[i+1]) < int(str_num[i+1] + str_num[i]):
#                 tmp = str_num[i+1]
#                 str_num[i+1] = str_num[i]
#                 str_num[i] = tmp
#             else:
#                 cur -= 1
#     print(str_num)
#
#     for num in str_num:
#         answer += num
#
#     print('answer', answer)
#     return answer

solution([6, 10, 2])
solution([3, 30, 34, 5, 9])