from itertools import permutations

# GPT
def is_prime(x: int) -> bool:
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 2
    return True

def solution(numbers: str) -> int:
    made = set()
    n = len(numbers)

    for r in range(1, n + 1):
        for p in permutations(numbers, r):
            made.add(int(''.join(p)))  # leading zero도 int가 처리해줌 (예: "011" -> 11)

    answer = 0
    for x in made:
        if is_prime(x):
            answer += 1

    print(answer)
    return answer

# Programmers

# from itertools import permutations
# def solution(n):
#     a = set()
#     for i in range(len(n)):
#         a |= set(map(int, map("".join, permutations(list(n), i + 1))))
#     a -= set(range(0, 2))
#     for i in range(2, int(max(a) ** 0.5) + 1):
#         a -= set(range(i * 2, max(a) + 1, i))
#     return len(a)