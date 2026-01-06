import collections


def solution(participant, completion):
    print(list(collections.Counter(participant)-collections.Counter(completion))[0])
    answer = (collections.Counter(participant)-collections.Counter(completion)).keys()
    print(answer)
    return answer

solution(["leo", "kiki", "eden"], ["eden", "kiki"])