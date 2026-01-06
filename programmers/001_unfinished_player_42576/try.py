def solution(participant, completion):
    candidates = participant[:]

    # for i in participant:
    #     if i in completion:
    #         candidates.remove(i)

    for c in completion:
        candidates.remove(c)

    answer = candidates[0]
    print(answer)
    return answer

solution(["leo", "kiki", "eden"], ["eden", "kiki"])