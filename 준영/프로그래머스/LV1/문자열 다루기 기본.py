def solution(s):
    answer = False
    if len(s) == 4 or len(s) == 6:
        if s.isdigit():
            answer = True
    return answer