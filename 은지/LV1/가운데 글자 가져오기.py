def solution(s):
    # 단어의 길이가 홀수
    if len(s) % 2:
        answer = s[len(s)//2]
    # 단어의 길이가 짝수
    else:
        answer = s[len(s)//2-1:len(s)//2+1]
    return answer