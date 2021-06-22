def solution(s):
    answer = True
    if len(s) != 4 and len(s) != 6:
        answer = False
    for x in s:
        if x.isnumeric() == False:
            answer = False
            break
    return answer