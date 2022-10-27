# https://school.programmers.co.kr/learn/courses/30/lessons/42583


def solution_failed(bridge_length, weight, truck_weights):
    passing = [0] * bridge_length
    seconds = 0

    while passing:
        seconds += 1

        if truck_weights:
            if sum(passing) + truck_weights[0] <= weight:
                passing.append(truck_weights.pop(0))
            else:
                passing.append(0)

    return seconds


def solution(bridge_length, weight, truck_weights):
    passing = [0] * bridge_length
    passing_weight = 0
    seconds = 0

    while passing:
        seconds += 1
        passing_weight -= passing.pop(0)

        if truck_weights:
            if passing_weight + truck_weights[0] <= weight:
                p = truck_weights.pop(0)
                passing.append(p)
                passing_weight += p
            else:
                passing.append(0)

    return seconds


print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
print(solution(100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]))
