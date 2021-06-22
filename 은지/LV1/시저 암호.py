def solution(s, n):
    answer = ''
    for x in s:
        # 공백인 경우
        if x == ' ':
            answer += ' '
        # 다시 돌아가야하는 경우
        # 1. 대문자
        elif 65 <= ord(x) <= 90 and ord(x) + n > 90:
            answer += chr(ord(x) + n - 26)
        # 2. 소문자
        elif 97 <= ord(x) <= 122 and ord(x) + n > 122:
            answer += chr(ord(x) + n - 26)
        # 돌아갈 필요없는 경우
        else:
            answer += chr(ord(x) + n)
    return answer