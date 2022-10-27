# https://school.programmers.co.kr/learn/courses/30/lessons/42576

import collections


# My solution
def solution(participant, completion):
    dic = collections.defaultdict(int)
    for p in participant:
        dic[p] += 1
    for c in completion:
        dic[c] -= 1
        if dic[c] == 0: dic.pop(c)
    return dic.popitem()[0]


# Other Solutions
def other_solution(participant, completion):
    count = collections.Counter(participant) - collections.Counter(completion)
    return count.popitem()[0]


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))  # "leo"
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))  # "vinko"
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))  # "mislav"
