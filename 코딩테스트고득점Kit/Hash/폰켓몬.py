# https://school.programmers.co.kr/learn/courses/30/lessons/1845

from collections import Counter


def solution(nums):
    N = len(nums) // 2
    pocketmon = Counter(nums)
    return min(N, len(pocketmon))
