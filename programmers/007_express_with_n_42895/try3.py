# Solved - Done
def solution(N, number):
    if N == number:
        return 1

    dp = [set() for _ in range(9)]

    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
        for j in range(1, i):
            k = i - j
            for a in dp[j]:
                for b in dp[k]:
                    dp[i].add(a+b)
                    dp[i].add(a-b)
                    dp[i].add(a*b)
                    if b != 0:
                        dp[i].add(a//b)
    print(dp)
    for l in range(1, 9):
        if number in dp[l]:
            return l

    answer = -1
    return answer

solution(5, 12)
solution(2, 11)