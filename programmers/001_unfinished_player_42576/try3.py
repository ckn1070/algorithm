# Solved - Done
from collections import defaultdict

def solution(participant, completion):
    d = defaultdict(int)
    for p in participant:
        d[p] += 1
    for c in completion:
        d[c] -= 1

    answer = ''
    for k in d.keys():
        if d[k] > 0:
            answer += k
    print(answer)
    return answer

solution(["leo", "kiki", "eden"], ["eden", "kiki"])
solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"])