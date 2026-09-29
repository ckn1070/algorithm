# Almost Solved
# 15/16 딱 하나는 뭐지
def solution(citations):
    citations.sort()
    answer = 0
    print('init', citations, answer)

    # 이 경계 때문에 (<= -> <) 딱 하나 틀림;;
    while answer < len(citations):
        nxt = len(citations) - (answer + 1)
        if citations[nxt] > answer:
            answer += 1
        else:
            break

    print('answer', answer)
    return answer

solution([3, 0, 6, 1, 5])

solution([3, 0, 6, 1, 5, 7, 8])
solution([0, 0, 0, 0, 3])
solution([5, 5, 5, 5, 5, 5])
