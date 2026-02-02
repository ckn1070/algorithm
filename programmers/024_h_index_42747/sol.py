# GPT
def solution(citations):
    citations.sort()
    n = len(citations)

    answer = 0
    for i in range(n):
        if citations[i] >= n - i:
            answer = max(answer, n - i)

    return answer

# Programmers
# def solution(citations):
#     citations.sort(reverse=True)
#     answer = max(map(min, enumerate(citations, start=1)))
#     return answer