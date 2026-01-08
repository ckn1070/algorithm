from collections import defaultdict as dd

# NOT SOLVED
def solution(name):
    al = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    cnt = dd(int)

    for idx, val in enumerate(al):
        if idx + 1 < 14:
            cnt[val] = idx
        else:
            cnt[val] = len(al) - idx

    answer = 0
    for i in name:
        print(i, cnt[i])
        print(name[1])
        answer += cnt[i]
    if (len(name) == 3 and name[1] == 'A') or name[0] == 'A':
        answer += 1
    else:
        answer += len(name) - 1

    print('ans: ', answer)
    return answer

solution("JEROEN")
solution("JAN")

# A가 가운데에 중복되어 있으면, 반대편으로 가는 것이 더 빠는 길일 수 있음