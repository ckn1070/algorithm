# NOT Solved
# 시간 초과..
# def solution(number, k):
#     numbers = []
#     for i in number:
#         numbers.append(int(i))
#     numbers.sort(reverse=True)
#
#     answer = ''
#     for j in numbers[:len(numbers)-k]:
#         answer += str(j)
#
#     print(answer)
#     return answer

def solution(number, k):
    answer = number

    def rec(num_str):
        maximum = '0'
        for i in range(len(num_str)):
            if i == 0:
                cur = num_str[1:]
            elif i == len(num_str) - 1:
                cur = num_str[:len(num_str) - 1]
            else:
                cur = num_str[:i] + num_str[i+1:]
            maximum = str(max(int(maximum), int(cur)))

        return maximum

    for j in range(k):
        answer = rec(answer)

    print(answer)
    return answer

solution("1924", 2)
solution("1231234", 3)
solution("4177252841", 4)