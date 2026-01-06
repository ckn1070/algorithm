# Programmers
def solution(ls):
    return min(len(ls)/2, len(set(ls)))

solution([3,1,2,3])
solution([3,3,3,2,2,4])
solution([3,3,3,2,2,2])