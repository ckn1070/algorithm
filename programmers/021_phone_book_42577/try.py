# NOT Solved
# 시간 초과..
def solution(phone_book):
    answer = True

    for i in phone_book:
        for j in phone_book:
            if i == j:
                continue
            if not answer:
                break

            if len(i) > len(j):
                continue
            else:
                sub = j[:len(i)]
                if i == sub:
                    print('i: ', i, 'j: ', j)
                    answer = False
                    break

    return answer

# def solution(phone_book):
#     answer = True
#     phone_book.sort(key=len)
#
#     for i, v1 in enumerate(phone_book):
#         for j, v2 in enumerate(phone_book):
#             if j <= i:
#                 continue
#             if not answer:
#                 break
#
#             else:
#                 sub = v2[:len(v1)]
#                 if v1 == sub:
#                     print('i: ', v1, 'j: ', v2)
#                     answer = False
#                     break
#
#     return answer

solution(["119", "97674223", "1195524421"])
solution(["123","456","789"])
solution(["12","123","1235","567","88"])