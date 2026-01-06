from functools import cmp_to_key

# GPT
def solution(numbers):
    arr = list(map(str, numbers))

    def cmp(a, b):
        if a + b > b + a:
            return -1
        if a + b < b + a:
            return 1
        return 0

    arr.sort(key=cmp_to_key(cmp))
    answer = ''.join(arr)
    return '0' if answer[0] == '0' else answer

# Programmers
# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=lambda x: x*3, reverse=True)
#     return str(int(''.join(numbers)))

# GPT
# (코테에서 제일 흔한) 문자열 반복 key로 정렬
# 보통 입력이 0~1000 범위라면 이렇게 합니다.
# 왜 x*3이 되나요?
# 자릿수가 달라서 "3" vs "30" 같은 비교가 깨지는데,
# "3"*3 = "333", "30"*3 = "303030" 처럼 비교 길이를 비슷하게 맞춰 붙이는 순서가 올바르게 나오게 합니다.
# (제한이 더 크면 *4, *10처럼 최대 자릿수에 맞춰 늘리면 됩니다.)
# def solution(numbers):
#     str_arr = list(map(str, numbers))
#     str_arr.sort(key=lambda x: x*3, reverse=True)  # 핵심!
#     answer = ''.join(str_arr)
#
#     # 엣지케이스: [0,0,0] -> "000"이 아니라 "0"
#     return '0' if answer[0] == '0' else answer