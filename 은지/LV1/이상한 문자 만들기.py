def solution(s):
    answer = ''
    i = 0
    for x in s:
        # 띄어쓰기 => i = 0
        if x == " ":
            answer += x
            i = 0
        # 문자
        else:
            if i % 2 == 0:
                answer += x.upper()
            else:
                answer += x.lower()
            i += 1
    return answer