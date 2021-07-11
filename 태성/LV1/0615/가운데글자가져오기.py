s = "abcde"

def solution(s):
    answer = ''
    m = len(s)//2
    if len(s) % 2 == 1:
        answer = s[m]

    else:
        answer += s[m-1]
        answer += s[m]
    return answer

print(solution(s))