def solution(s):
    answer = ''
    n = 0
    for ss in s:
        if ss == ' ':
            answer += ss
            n = 0
        else:
            if n%2 == 0:
                answer += ss.upper()
                n += 1
            else:
                answer += ss.lower()
                n += 1
    return answer