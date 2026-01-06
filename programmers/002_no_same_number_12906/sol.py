def solution(arr):
    answer = []

    for num in arr:
        # 1. answer가 비어있으면 무조건 추가 (첫 번째 숫자)
        # 2. answer의 마지막 숫자(answer[-1])가 현재 숫자(num)와 다르면 추가
        if len(answer) == 0 or answer[-1] != num:
            answer.append(num)

    print(answer)
    return answer

solution([1,1,3,3,0,1,1])
solution([4,4,4,3,3])