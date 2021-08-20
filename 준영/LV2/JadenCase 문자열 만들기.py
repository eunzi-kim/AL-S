def solution(s):
    answer = ''
    idx = 0
    for i in s:
        if i == ' ':
            answer += i
            idx = 0
            continue

        if idx == 0:
            answer += i.upper()
            idx += 1
        else:
            answer += i.lower()

    return answer

s = "3people unFollowed me"	
solution(s)
s = "aaaaa aaa "
solution(s)