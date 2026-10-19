# Solved
# 뭐지? 예시는 깔끔하게 맞았는데 테스트는 싹 다 실패라고?
# 0/5, 0/5 -> 정답
# 아 포함되는 차량을 처리를 못하는건가? 1 ~ 10, 3 ~ 5 - 그럼 오른쪽 끝 점 순서로 정렬해야하나?
# 와 이거 한 줄에 정답이네;
from collections import deque

def solution(routes):
    routes.sort(key=lambda x: x[1]) # 이거 하나에 정답
    cam = -50_000
    q = deque()

    cnt = 0
    for s, e in routes:
        while q:
            ci, co = q.popleft()
            if ci <= cam <= co:
                print('pass', ci, co, cam, cnt)
                continue
            cam = co
            cnt += 1
            print('loop', ci, co, cam, cnt)
        q.append((s, e))

    while q:
        ci, co = q.popleft()
        if ci <= cam <= co:
            print('pass', ci, co, cam, cnt)
            continue
        cam = co
        cnt += 1

    answer = cnt
    return answer

solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]])