# Not Solved
#
# 괄호나 사칙연산의 위치를 기반으로 계산하는건 비현실적
# - 너무 경우의 수가 많고, 동일한 계산 결과가 지나치게 많이 나올 수 있다
#
# 개수가 결국 Return 값이니, 각 개수별로 표현 가능한 숫자를 DP
# - 중복이 생길 수 있으니 Set
#
# 최댓값이 정해져있으니 거기까지만 Loop을 돌면서,
# 그만큼 숫자를 붙인걸 DP에 넣고
def solution(N, number):
    if N == number:
        return 1

    dp = [set() for _ in range(9)]

    for i in range(1, 9):
        dp[i].add(int(str(N)*i))

        for j in range(1, i+1):
            for a in dp[j]:
                for b in dp[i-j]:
                    dp[i].add(a+b)
                    dp[i].add(a-b)
                    dp[i].add(a*b)
                    if b != 0:
                        dp[i].add(a//b)

        if number in dp[i]:
            print('i', i, N, number)
            return i


    return -1


# Programmers
# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
# def solution(N, number):
#     S = [{N}]
#     for i in range(2, 9):
#         lst = [int(str(N)*i)]
#         for X_i in range(0, int(i / 2)):
#             for x in S[X_i]:
#                 for y in S[i - X_i - 2]:
#                     lst.append(x + y)
#                     lst.append(x - y)
#                     lst.append(y - x)
#                     lst.append(x * y)
#                     if x != 0: lst.append(y // x)
#                     if y != 0: lst.append(x // y)
#         if number in set(lst):
#             return i
#         S.append(lst)
#     return -1



solution(5, 12)
solution(2, 11)