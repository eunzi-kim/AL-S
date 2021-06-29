def solution(s):
    answer = 0
    stack = []
    for x in s:
        if len(stack):
            v = stack.pop(-1)
            if x != v:
                stack.append(v)
                stack.append(x)
        else:
            stack.append(x)
    if len(stack) == 0:
        answer = 1
    return answer

s = "baabaa"
print(solution(s))