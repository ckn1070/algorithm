def solution(sizes):
    answer = 0

    arr = []
    for size in sizes:
        arr.append(size[0])
        arr.append(size[1])
    arr.sort()

    w = arr[-1]

    def rec(height):
        tmp = height
        for s in sizes:
            print('s', s)
            st = sorted(s)
            if s[0] > height and s[1] > height:
                print('tmp', st[0])
                tmp = st[0]
                rec(tmp)
                break
        return tmp


    h = rec(arr[0])
    print('rec', rec(arr[0]))
    answer = w*h

    print('w', w)
    print('h', h)
    print('answer', answer)
    return answer

# solution([[60, 50], [30, 70], [60, 30], [80, 40]])
solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]])
# solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]])