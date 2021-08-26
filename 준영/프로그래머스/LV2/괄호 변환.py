def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

def check_proper(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0:
                return False
            count -= 1
    return True # 쌍이 맞는 경우에 True 반환

def solution(p):
    # 1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다.
    answer = ''
    if p == '':
        return answer
    
    # 문자열 p를 두 "균형잡힌 괄호 문자열" u, v 로 분리합니다.
    # 단, usms "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며,
    # v는 빈 문자열이 될 수 있습니다
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]
    if check_proper(u):
        # 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다.
        # 문자열 u가 "올바른 괄호 문자열"이라면 문자열 v에 대해 1단계부터 다시 수행합니다.
        answer = u + solution(v)
    # 문자열 u가 올바른 문자열이 아니라면 아래 과정을 수행합니다.
    else:
        # 빈 문자열에 첫 번째 문자로 '('를 붙입니다.
        answer = '('
        # 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다.
        answer += solution(v)
        # ')'를 다시 붙입니다.
        answer += ')'
        # u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다.
        u = list(u[1:-1])
        
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += ''.join(u)
    return answer