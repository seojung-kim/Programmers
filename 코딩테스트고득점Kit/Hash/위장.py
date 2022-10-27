# https://school.programmers.co.kr/learn/courses/30/lessons/42578

from collections import defaultdict


def solution(clothes):
    dic = defaultdict(list)
    for cloth_name, cloth_type in clothes:
        dic[cloth_type].append(cloth_name)
    answer = 1
    for cloth_type in dic:
        answer *= len(dic[cloth_type]) + 1
    return answer - 1


print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
