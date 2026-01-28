# NOT Solved
# 뭔가 애매하게 틀림..
from collections import defaultdict as dd

def solution(genres, plays):
    total = dd(list) # play, i
    cnt = dd(int)
    time = []
    ids = dd(int)

    for i, v in enumerate(genres):
        total[v].append((plays[i], i))
        time.append((plays[i], i, v))

    time.sort(key=lambda x: (-x[0], x[1]))

    answer = []
    res = []
    uid = 1
    for t, n, g in time:
        if ids[g] == 0:
            ids[g] = uid
            uid += 1
        if cnt[g] < 2:
            cnt[g] += 1
            res.append((ids[g], t, n))

    res.sort(key=lambda x: (x[0], -x[1]))
    print(res)
    for j in res:
        answer.append(j[2])

    # mp = []
    # for k in total.keys():
    #     total[k].sort(key=lambda x: (-x[0], x[1]))
    #     mp.append((total[k][0][0], k))
    # print(total)
    #
    # mp.sort(reverse=True)
    # print(mp)
    #
    # for p in mp:
    #     answer.append(total[p[1]][0][1])
    #     if total[p[1]][1][1] >= 0:
    #         answer.append(total[p[1]][1][1])

    print(answer)
    return answer

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])