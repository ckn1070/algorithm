# Solved
from collections import defaultdict as dd

def solution(participant, completion):
    cnt = dd(int)
    for i in participant:
        cnt[i] += 1
    for j in completion:
        cnt[j] -= 1

    for k in cnt:
        if cnt[k] == 1:
            answer = k

    print(answer)
    return answer

solution(["leo", "kiki", "eden"], ["eden", "kiki"])
solution(["marina", "josipa", "nikola", "vinko", "filipa"],["josipa", "filipa", "marina", "nikola"])
solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"])


# Programmers
# import collections
#
#
# def solution(participant, completion):
#     Counter: 리스트 안의 각 값이 몇 번 나오는지 세어주는 객체
#     Counter끼리 빼면 각 이름의 개수를 서로 빼고, 0 이하인 항목은 제거 (양수만 남김)
#     answer = collections.Counter(participant) - collections.Counter(completion)
#     return list(answer.keys())[0]
