# https://school.programmers.co.kr/learn/courses/30/lessons/42586

from math import ceil


def solution(progresses, speeds):
    work_days = [ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    answer = [1]
    temp = work_days[0]  # 배포까지 남은 일수
    for i in range(1, len(work_days)):
        if temp >= work_days[i]:
            answer[-1] += 1
        else:
            temp = work_days[i]
            answer.append(1)
    return answer


print(solution([93, 30, 55], [1, 30, 5]))  # [2, 1]
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))  # [1, 3, 2]
