# GPT
import math

def solution(progresses, speeds):
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]

    answer = []
    cur = days[0]
    cnt = 1

    for d in days[1:]:
        if d <= cur:
            cnt += 1
        else:
            answer.append(cnt)
            cur = d
            cnt = 1

    answer.append(cnt)
    return answer

# Programmers
# def solution(progresses, speeds):
#     Q=[]
#     for p, s in zip(progresses, speeds):
#         if len(Q)==0 or Q[-1][0]<-((p-100)//s):
#             Q.append([-((p-100)//s),1])
#         else:
#             Q[-1][1]+=1
#     return [q[1] for q in Q]