# Solved
def solution(arr):
    answer = []

    st = []
    for i in range(0, len(arr)):
        answer.append(arr[i])
        st.append(arr[i])

        if len(st) > 1 and (st[-1] == st[-2]):
            answer.pop()

    print(answer)
    return answer

solution([1,1,3,3,0,1,1])
solution([4,4,4,3,3])