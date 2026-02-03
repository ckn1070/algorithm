# Solved
def solution(word):
    given = ['A', 'E', 'I', 'O', 'U']
    uq = set()

    def rec(n, sub):
        for i in given:
            if len(sub) < n:
                rec(n, sub + i)
        uq.add(sub)
        return sub

    for j in range(1, 6):
        rec(j, '')

    dic = sorted(list(uq))
    print(dic.index(word))

    return dic.index(word)

solution("AAAAE")
solution("AAAE")
solution("I")
solution("EIO")