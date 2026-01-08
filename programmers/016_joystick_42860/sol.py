# GPT
def solution(name: str) -> int:
    n = len(name)

    # 1) 알파벳 변경(위/아래) 비용
    # ord(): 문자(char)를 해당하는 유니코드(정수) 값으로 바꿔주는 파이썬 내장 함수
    change = 0
    for ch in name:
        up = ord(ch) - ord('A')
        down = ord('Z') - ord(ch) + 1
        change += min(up, down)

    # 2) 커서 이동(좌/우) 최소 비용
    # 기본은 끝까지 오른쪽으로만 가는 경우: n-1
    move = n - 1

    for i in range(n):
        # i 다음부터 연속된 A가 끝나는 지점 next_idx 찾기
        next_idx = i + 1
        while next_idx < n and name[next_idx] == 'A':
            next_idx += 1

        # 케이스1: 오른쪽으로 i까지 갔다가 다시 돌아와서(왕복) 남은 오른쪽 끝 처리
        move = min(move, 2 * i + (n - next_idx))

        # 케이스2: 반대로(왼쪽 방향을 더 활용) 끝쪽을 먼저 처리하는 형태
        move = min(move, i + 2 * (n - next_idx))

    return change + move

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
