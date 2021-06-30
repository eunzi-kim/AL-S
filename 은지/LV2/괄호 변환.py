# 문자열 분리
def division(w):
    l = r = 0
    for i in range(len(w)):
        if w[i] == "(":
            l += 1
        else:
            r += 1
        if l == r:
            return w[:i+1], w[i+1:]


# 올바른 괄호 문자열 판별
def chk(s):
    stack = []
    for x in s:
        if x == "(":
            stack.append("(")
        else:
            if len(stack):
                stack.pop(-1)
    return len(stack)


def solution(p):
    answer = ''    
    # 올바른 괄호 문자열
    if chk(p) == 0:
        answer = p
    else:
        u, v = division(p)
        if chk(u) == 0:
            return u + solution(v)
        else:
            answer = '(' + solution(v) + ')'
            for i in range(1, len(u)-1):
                if u[i] == '(':
                    answer += ')'
                else:
                    answer += '('   
    return answer

p = "()))((()"
print(solution(p))