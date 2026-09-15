# Solved
# zip까진 좋았는데, 그 뒤로가 좀 깔끔하지 못한 것 같다..
# 근데 또 답 보니깐 Queue 대신 List 그대로 쓰는 것 말고는, 거의 비슷한 것 같기도 하네;
import math
from collections import deque as dq

def solution(progresses, speeds):
    duration = []

    for p, s in zip(progresses, speeds):
        end = math.ceil((100-p)/s)
        duration.append(end)

    print('duration', duration )
    q = dq(duration)
    answer = []
    nxt = q.popleft()
    cnt = 1
    while q:
        cur = q.popleft()
        print('cnt', cnt, cur)
        if cur > nxt:
            nxt = cur
            answer.append(cnt)
            cnt = 1
        else:
            cnt += 1

    if cnt != 0:
        answer.append(cnt)
    print('answer', answer)

    return answer

solution([93, 30, 55], [1, 30, 5])
solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])


# Programmers
# 문제가 개편되었습니다. 이로 인해 함수 구성이나 테스트케이스가 변경되어, 과거의 코드는 동작하지 않을 수 있습니다.
# 새로운 함수 구성을 적용하려면 [코드 초기화] 버튼을 누르세요. 단, [코드 초기화] 버튼을 누르면 작성 중인 코드는 사라집니다.
# def solution(progresses, speeds):
#     Q=[]
#     for p, s in zip(progresses, speeds):
#         if len(Q)==0 or Q[-1][0]<-((p-100)//s):
#             Q.append([-((p-100)//s),1])
#         else:
#             Q[-1][1]+=1
#     return [q[1] for q in Q]