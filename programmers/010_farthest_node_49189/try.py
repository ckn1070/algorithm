import collections

# NOT Solved
def solution(n, edge):
    counter = collections.defaultdict()

    def rec(cur, lst, cnt):
        for idx, i in enumerate(lst):
            print(idx, i)
            print(lst)
            print(counter)
            print('cur-', cur)
            if i[0] == cur:
                cnt += 1
                lst2 = lst[:]
                lst2.pop(idx)
                counter[i[1]] = cnt
                print('cur', cur)
                print('next', i[1])
                nxt = i[1]
                rec(nxt, lst2, cnt)


    for idx2, j in enumerate(edge):
        if j[0] == 1:
            count = 1
            edge.pop(idx2)
            rec(j[1], edge[:], count)
    answer = 0

    print(counter)
    return answer


solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
