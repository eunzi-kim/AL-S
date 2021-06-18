def solution(s):
    answer = ''
    temp = list(s)
    temp.sort(reverse=True)
    answer = "".join(temp)
    return answer

print(solution("Zbcdefg"))