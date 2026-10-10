# Solved
# 장르 별로 두 개
# 속한 노래가 많이 재생된 장르 순
# 장르 내에서 많이 재생된 노래 순
# 장르 내에서 재생 수가 같으면 고유 번호가 낮은 순
# 13/15? 이 애매한 2개는 뭐지 - 15/15
from collections import defaultdict

def solution(genres, plays):
    gen_play = defaultdict(int)
    gen_song = defaultdict(list)

    for i, (g, p) in enumerate(zip(genres, plays)):
        gen_play[g] += p
        gen_song[g].append((p, i))
    gen_total = [(gen_play[k], k) for k in gen_play.keys()]
    gen_total.sort(reverse=True) # 많이 재생된 장르 순
    print(gen_play, gen_song, gen_total)

    answer = []
    for val, key in gen_total:
        arr = gen_song[key]
        # 아 여기서 pop을하면 play가 같을 때 idx가 큰것부터 되겠구나;
        arr.sort(key=lambda x: (x[0], -x[1]))
        print('arr', arr)
        i = 0
        while i < 2 and arr:
            cur = arr.pop()
            answer.append(cur[1])
            i += 1

    print(answer)
    return answer

solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
solution(["classic", "pop", "classic", "classic", "kpop"], [500, 600, 150, 800, 2500])