# NOT Solved
def solution(numbers):
    # def rec(arr, cur):
    #     print(arr, cur)
    #     nonlocal maximum
    #     if len(arr) < 1:
    #         if int(cur) > maximum:
    #             maximum = int(cur)
    #     else:
    #         for i in range(len(arr)):
    #             cur + str(arr[i])
    #             tmp = arr[:]
    #             if len(tmp) > 0:
    #                 tmp.pop(i)
    #             print('tmp', tmp)
    #             rec(tmp, cur)

    # 런타임 에러
    # def rec(arr, cur):
    #     # 종료 조건
    #     if not arr:
    #         return int(cur)
    #
    #     results = []
    #     for i in range(len(arr)):
    #         next_cur = cur + str(arr[i])
    #         next_arr = arr[:]
    #         next_arr.pop(i)
    #
    #         results.append(rec(next_arr, next_cur))
    #
    #     return max(results)
    #
    # answer = rec(numbers, '')
    # print(answer)
    # return str(answer)
    str_arr = []
    for i in numbers:
        str_arr.append(str(i))
    str_arr.sort(reverse=True)

    cur = ''
    for i in str_arr:
        cur += i
    print(cur)
    return 1

solution([6, 10, 2])
solution([3, 30, 34, 5, 9])