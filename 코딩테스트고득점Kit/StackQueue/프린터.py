# https://school.programmers.co.kr/learn/courses/30/lessons/42587

# My solution
def solution(priorities, location):
    idx = [i for i in range(len(priorities))]
    answer = []
    while idx:
        p = idx.pop(0)
        if priorities[p] != max(priorities):
            idx.append(p)
        else:
            answer.append(p)
            priorities[p] = 0
    return answer.index(location) + 1


# Other solution
def solution02(priorities, location):
    queue = [(i, p) for i, p in enumerate(priorities)]
    answer = 0
    while True:
        p = queue.pop(0)
        if any(p[1] < q[1] for q in queue):
            queue.append(p)
        else:
            answer += 1
            if p[0] == location:
                return answer


print(solution([2, 1, 3, 2], 2))  # 1
print(solution([1, 1, 9, 1, 1, 1], 0))  # 5
print(solution([2, 3, 3, 2, 9, 3, 3], 3))  # 6
