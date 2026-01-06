# Programmers
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])

# GPT
# def solution(numbers, target):
#     def dfs(i, total):
#         if i == len(numbers):
#             return 1 if total == target else 0
#         return dfs(i + 1, total + numbers[i]) + dfs(i + 1, total - numbers[i])
#
#     return dfs(0, 0)

print(solution([1, 1, 1, 1, 1], 3))
solution([4, 1, 2, 1], 4)