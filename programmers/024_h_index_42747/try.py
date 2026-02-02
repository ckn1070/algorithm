# Solved
def solution(citations):
    citations.sort()
    print(citations)
    n = len(citations)

    answer = 0
    for i in range(min(citations[0], 0), min(citations[-1], len(citations))+1):
        cur = citations[n-i:]
        print('cur', cur, n, i)
        if len(cur) == 0:
            continue
        if i <= cur[0]:
            answer = i

    print (answer)
    return answer

solution([3, 0, 6, 1, 5])