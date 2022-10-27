# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    cnt = 0
    for i in s:
        cnt += 1 if i == '(' else -1
        if cnt < 0: return False
    return True if cnt == 0 else False


def solution02(s):
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            try:
                stack.pop()
            except IndexError:
                return False

    return True if len(stack) == 0 else False