def solution(s):
    answer = 0
    # 음수인 경우
    if s[0] == '-':
        answer = int(s[1:]) * (-1)
    # 양수인 경우
    else:
        answer = int(s)
    return answer