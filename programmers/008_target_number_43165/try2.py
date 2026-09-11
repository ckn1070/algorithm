# Solved
# 근데 개판.. 심지어 처음보다도 못풀었네
#
# 끝까지 계산을 해봐야하니, DFS로 가야하는 것은 알겠는데, 어떻게..?
#
# 중간 결과를 알 필요 없이, 최종 결과가 Target과 동일한지만 파악하면 되니,
# Return 값을 바로 계산하도록 구성
# 처음 한 번만 호출하면, 모든 경우의 수가 다 더해지도록
# 그럼 DFS에는 현재 위치와 현재 값을 알 수 있도록 전달돼야겠네
def solution(numbers, target):

    def dfs(i, total):
        if i == len(numbers):
            return 1 if total == target else 0

        return dfs(i + 1, total + numbers[i]) + dfs(i + 1, total - numbers[i])

    answer = dfs(0, 0)
    print('answer', answer)
    return answer

# def solution(numbers, target):
#     result = [[] for _ in range(len(numbers)+1)]
#     result[0].append(0)
#
#     def rec(bf, nxt, res):
#         res.append(bf + nxt)
#         res.append(bf - nxt)
#
#     for i, cur in enumerate(numbers):
#         for j in result[i]:
#             rec(j, cur, result[i+1])
#
#     print('res', result)
#
#     answer = 0
#     for k in result[len(numbers)]:
#         if k == target:
#             answer += 1
#
#     print('ans', answer)
#
#     return answer

solution([1, 1, 1, 1, 1], 3)
solution([4, 1, 2, 1], 4)


# Programmers
# def solution(numbers, target):
#     if not numbers and target == 0 :
#         return 1
#     elif not numbers:
#         return 0
#     else:
#         return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])