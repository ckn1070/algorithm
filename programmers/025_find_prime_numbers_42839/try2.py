# NOT Solved
# 조합도 문제고, 소수찾기도 문제인데..? 진짜 총체적 난국;
#
# Permutation 사용까지는 생각해냈다
# 소수는 내가 만들어야한다 - 딱히 방법이 없다
# 하긴 이것까지 있었으면 알고리즘이 아니라 그냥 라이브러리 사용이지
#
# 그럼 itertools가 없다면?
# DFS로 끝까지 가면서 숫자 만들기 - set에 넣기
#
# 전부 다 나눠봐야 하는건 어차피 아니고,
# x = a^2라고 했을 때 (루트), a보다 작은 수 * a보다 큰 수로 이루어질 것이기 때문에,
# a까지만 해보면 소수인지 아닌지 판단이 가능
#
# Try 2
from itertools import permutations

def solution(numbers):
    def is_prime(x):
        if x < 2:
            return False
        elif x == 2:
            return True
        elif x % 2 == 0:
            return False

        i = 3
        while i * i <= x:
            if x % i == 0:
                return False
            i += 1

        return True

    candidates = set()
    for i in range(len(numbers)):
        total = permutations(numbers, i + 1)
        for p in total:
            candidates.add(int(''.join(p)))
            print('candidates', candidates)

    answer = 0
    for c in candidates:
        if is_prime(c):
            answer += 1

    print('answer', answer)
    return answer


# Try 1
# from itertools import permutations, combinations
#
# def solution(numbers):
#     a = combinations(numbers, 2)
#     print(list(a))
#
#     answer = 0
#     return answer

solution("17")
solution("011")