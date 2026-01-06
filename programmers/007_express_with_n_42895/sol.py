# Difficult
# Gemini
def solution(N, number):
    if N == number:
        return 1

    # index 1부터 8까지 사용하기 위해 크기 9의 리스트 생성
    # s[i]는 N을 i번 사용해서 만들 수 있는 수들의 집합
    s = [set() for _ in range(9)]

    for i in range(1, 9):
        # 1. N, NN, NNN... 형태 추가 (예: 5, 55, 555)
        s[i].add(int(str(N) * i))

        # 2. 이전 단계의 집합들을 사칙연산으로 조합
        # j는 1부터 i-1까지 (예: i가 4면, (1,3), (2,2), (3,1) 조합을 확인)
        for j in range(1, i):
            for op1 in s[j]:
                for op2 in s[i - j]:
                    s[i].add(op1 + op2)
                    s[i].add(op1 - op2)
                    s[i].add(op1 * op2)
                    if op2 != 0:
                        s[i].add(op1 // op2)  # 문제에 따라 나눗셈은 정수 부분만 취하거나 일반 나눗셈을 함

        # 3. 목표 숫자가 현재 집합에 있는지 확인
        if number in s[i]:
            return i

    return -1

# GPT
# def solution(N, number):
#     # N 하나만 써도 되는 경우
#     if N == number:
#         return 1
#
#     # dp[i] : N을 i번 사용해서 만들 수 있는 수들의 집합
#     dp = [set() for _ in range(9)]  # 0은 안 씀, 1~8만 사용
#
#     for i in range(1, 9):
#         # 예: N=5, i=3 → 555
#         repeated = int(str(N) * i)
#         dp[i].add(repeated)
#
#         # j + (i-j) 개로 나누어 두 집합의 수들을 사칙연산으로 조합
#         for j in range(1, i):
#             for a in dp[j]:
#                 for b in dp[i - j]:
#                     dp[i].add(a + b)
#                     dp[i].add(a - b)
#                     dp[i].add(a * b)
#                     if b != 0:
#                         dp[i].add(a // b)
#
#         # 이번 단계에서 목표 숫자를 만들 수 있으면 바로 반환
#         if number in dp[i]:
#             return i
#
#     # 8개까지 다 써도 못 만들면 -1
#     return -1

# Programmers
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

print(solution(5, 12))
# solution(2, 11)
