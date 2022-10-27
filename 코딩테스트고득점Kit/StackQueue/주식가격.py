"""
def solution(prices):
    length = len(prices)
    seconds = [0] * length
    for i in range(length):
        for j in range(i + 1, length):
            seconds[i] += 1
            if prices[i] > prices[j]:
                break
    return seconds
"""


def solution(prices):
    length = len(prices)
    answer = []
    for i in range(length):
        for j in range(i + 1, length):
            if prices[i] > prices[j]:
                break
        answer.append(j - i)

    return answer


print(solution([1, 2, 3, 2, 3]))  # [4,3,1,1,0]
