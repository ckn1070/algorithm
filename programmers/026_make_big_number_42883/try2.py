# NOT Solved
# 개수가 많아서 로직을 찾는게 맞는데..
#
# Stack 개념까진 떠올렸는데..
#
# 앞에서부터 숫자를 받고,
# 받은 숫자를 넣기 전에, 뒤에서부터 훑으면서 그 숫자보다 작은 숫자들을 없애고
# Try 3
def solution(number, k):
    st = []
    cnt = k

    for i in number:
        while st and cnt > 0 and st[-1] < i:
            cnt -= 1
            st.pop()
        st.append(i)

    while cnt > 0:
        cnt -= 1
        st.pop()

    answer = ''.join(st)
    print(answer)
    return answer


# Try 2
# def solution(number, k):
#     n = len(number)
#     st = []
#     for i in range(n):
#         st.append(number[n-1-i])
#     print(st)
#
#     cnt = k
#     res = []
#     while len(st) > 1 and cnt > 0:
#         cur = st.pop()
#         nxt = st.pop()
#         print('cur', cnt, cur, nxt)
#         if cur < nxt:
#             cnt -= 1
#             st.append(nxt)
#             print('nxt', cnt, st)
#         elif cur > nxt:
#             cnt -= 1
#             st.append(cur)
#             print('nxt2', st)
#
#     answer = ''
#     return answer


# Try 1
# def solution(number, k):
#     init = k
#     answer = ''
#
#     for i in range(len(number) - 1):
#         print('i', i, number[i], number[i + 1])
#         if init == 0:
#             answer += str(number[i:])
#             break
#
#         if number[i] < number[i + 1]:
#             init -= 1
#         else:
#             answer += str(number[i])
#
#     print('tmp', number, answer)
#     return answer

solution("1924", 2)
solution("1231234", 3)
solution("4177252841", 4)