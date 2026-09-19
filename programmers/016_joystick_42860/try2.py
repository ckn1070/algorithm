# NOT Solved
#
# 번호는 ASCII로 찾으면 편할 것 같은데, 방법이 기억이 안난다;
# 연속된 A를 찾는다는 개념도 맞게 생각하긴 했는데..
#
# Try 2
def solution(name):

    cnt = 0
    for ch in name:
        up = ord(ch) - ord('A')
        down = ord('Z') - ord(ch) + 1
        cnt += min(up, down)
    print('cnt', cnt)

    n = len(name)
    move = n - 1
    for i in range(n):
        nxt = i + 1
        while nxt < n and name[nxt] == 'A':
            nxt += 1

        move = min(move, i * 2 + (n - nxt))
        move = min(move, i + 2 * (n - nxt))

    print('move', move, cnt)
    answer = cnt + move
    return answer


# Try 1
# def solution(name):
#     al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     def findword(word):
#         up = al.find(word)
#         down = len(al) - up
#         return min(up, down)
#
#     node = [0] * len(name)
#     cnt = 0
#     for i, c in enumerate(name):
#         if c != 'A':
#             node[i] = 1
#         cnt += findword(c)
#     node[0] = 0
#     print('node', node)
#     print('cnt', cnt)
#
#     answer = 0
#     return answer

solution("JEROEN")
solution("JAN")
solution("JERAAOEN")


# Programmers
# def solution(name):
#     answer = 0
#     n = len(name)
#
#     def alphabet_to_num(char):
#         num_char = [i for i in range(14)] + [j for j in range(12, 0, -1)]
#         return num_char[ord(char) - ord('A')]
#
#     for ch in name:
#         answer += alphabet_to_num(ch)
#
#     move = n - 1
#     for idx in range(n):
#         next_idx = idx + 1
#         while (next_idx < n) and (name[next_idx] == 'A'):
#             next_idx += 1
#         distance = min(idx, n - next_idx)
#         move = min(move, idx + n - next_idx + distance)
#
#     answer += move
#     return answer