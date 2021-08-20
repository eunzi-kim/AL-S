def solution(s):
    answer = ''
    for i in range(len(s)):
        if i == 0:
            answer += s[i].upper()
        elif s[i-1] == " ":
            answer += s[i].upper()
        else:
            answer += s[i].lower()
    return answer

s = "3people unFollowed me"
print(solution(s))