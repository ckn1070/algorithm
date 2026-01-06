# Solved
def solution(nums):
    nums.sort()
    n = int(len(nums)/2)
    res = []

    for i in range(len(nums)):
        print('res', res)

        if len(res) == 0:
            res.append(nums[i])
            continue

        if res[-1] != nums[i]:
            res.append(nums[i])
            print(res)

    answer=min(n, len(res))
    print(answer)
    return answer

solution([3,1,2,3])
solution([3,3,3,2,2,4])
solution([3,3,3,2,2,2])