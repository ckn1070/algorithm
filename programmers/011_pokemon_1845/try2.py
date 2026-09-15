# Solved
# 굉장히 깔끔하게 잘 푼듯?
def solution(nums):
    answer = min(len(set(nums)), len(nums)/2)
    print('answer', answer)
    return int(min(len(set(nums)), len(nums)/2))

solution([3,1,2,3])
solution([3,3,3,2,2,4])
solution([3,3,3,2,2,2]	)