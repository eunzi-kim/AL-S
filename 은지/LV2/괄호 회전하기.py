import copy

# 괄호 체크 함수
def chk(l):
    lst = copy.deepcopy(l)
    # 괄호 짝지어서 없애주기
    i = 0
    while i < len(lst)-1: 
        if lst[i] == "(" and lst[i+1] == ")":
            # 괄호 없애기
            lst.pop(i)
            lst.pop(i)
            # 감싼 괄호 확인 위해 앞으로 가기
            if i > 0:
                i -= 1
        elif lst[i] == "{" and lst[i+1] == "}":
            lst.pop(i)
            lst.pop(i)
            if i > 0:
                i -= 1
        elif lst[i] == "[" and lst[i+1] == "]":
            lst.pop(i)
            lst.pop(i)
            if i > 0:
                i -= 1
        # 괄호 없으면 뒤로 가기
        else:
            i += 1
    # 괄호 체크하고 남은 리스트 반환
    return len(lst)

def solution(s):
    answer = 0
    # 문자열 => 배열
    lst_s = [x for x in s]
    # len(s)번의 경우의 수
    for _ in range(len(s)):
        # 모든 괄호 없애는 경우 +1
        if chk(lst_s) == 0:
            answer += 1
        # 괄호 회전
        v = lst_s.pop(0)
        lst_s.append(v)
    return answer

s = "}]()[{"
print(solution(s))