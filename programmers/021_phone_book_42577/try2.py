# Solved
# Try 2
def solution(phone_book):
    phone_book.sort()
    print(phone_book)

    answer = True
    for i in range(len(phone_book) - 1):
        cur = phone_book[i]
        nxt = phone_book[i+1]
        if len(nxt) > len(cur) and cur == nxt[:len(cur)]:
            print('search', cur, nxt)
            answer = False
    return answer


# Try 1
# 정확성 20/20, 효율성 2/4
# def solution(phone_book):
#     phone_book.sort(key=len)
#
#     answer = True
#     for i in range(len(phone_book)):
#         cur = phone_book[i]
#         for j in range(i+1, len(phone_book)):
#             nxt = phone_book[j]
#             print('cur', cur, nxt, nxt[:len(cur)])
#             if len(cur) < len(nxt) and cur == nxt[:len(cur)]:
#                 print('answer', cur, nxt)
#                 answer = False
#                 break
#         if not answer:
#             break
#
#     return answer


# Programmers
# def solution(phone_book):
#     answer = True
#     hash_map = {}
#     for phone_number in phone_book:
#         hash_map[phone_number] = 1
#     for phone_number in phone_book:
#         temp = ""
#         for number in phone_number:
#             temp += number
#             if temp in hash_map and temp != phone_number:
#                 answer = False
#     return answer

solution(["119", "97674223", "1195524421"])
solution(["123","456","789"])
solution(["12","123","1235","567","88"])

solution(["119", "1195524421", "97674223"])
solution(["12", "15", "14", "13","123","1235","567","88"])