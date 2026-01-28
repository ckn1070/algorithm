# GPT
from collections import defaultdict

def solution(genres, plays):
    genre_sum = defaultdict(int)
    songs = defaultdict(list)  # genre -> [(plays, idx), ...]

    for idx, (g, p) in enumerate(zip(genres, plays)):
        genre_sum[g] += p
        songs[g].append((p, idx))

    # 장르별 곡 정렬: 재생수 desc, idx asc
    for g in songs:
        songs[g].sort(key=lambda x: (-x[0], x[1]))

    # 장르 정렬: 총 재생수 desc
    ordered_genres = sorted(genre_sum.keys(), key=lambda g: -genre_sum[g])

    answer = []
    for g in ordered_genres:
        answer.append(songs[g][0][1])
        if len(songs[g]) > 1:
            answer.append(songs[g][1][1])

    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))

# GPT
# def solution(genres, plays):
#     answer = []
#     d = {e:[] for e in set(genres)}
#     for e in zip(genres, plays, range(len(plays))):
#         d[e[0]].append([e[1] , e[2]])
#     genreSort =sorted(list(d.keys()), key= lambda x: sum( map(lambda y: y[0],d[x])), reverse = True)
#     for g in genreSort:
#         temp = [e[1] for e in sorted(d[g],key= lambda x: (x[0], -x[1]), reverse = True)]
#         answer += temp[:min(len(temp),2)]
#     return answer