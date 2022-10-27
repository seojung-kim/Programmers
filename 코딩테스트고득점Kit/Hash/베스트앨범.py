# https://school.programmers.co.kr/learn/courses/30/lessons/42579

from collections import defaultdict


def solution(genres, plays):
    genres_dic = defaultdict(list)
    genres_cnt = defaultdict(int)

    for i in range(len(genres)):
        genres_dic[genres[i]].append(i)
        genres_cnt[genres[i]] += plays[i]
    genres_cnt = sorted(genres_cnt, key=lambda x: genres_cnt[x], reverse=True)

    answer = []
    for genre in genres_cnt:
        genres_dic[genre].sort(key=lambda x: plays[x], reverse=True)
        answer += genres_dic[genre][:2] if len(genres_dic[genre]) > 2 else genres_dic[genre]
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
