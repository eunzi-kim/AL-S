def solution(s):
    stack = []
    for x in s:
        if len(stack) == 0:
            if x == ")":
                return False
            else:
                stack.append(x)
        else:
            if x == "(":
                stack.append(x)
            else:
                stack.pop(-1)
    if len(stack):
        return False
    return True

s = "(()("
print(solution(s))