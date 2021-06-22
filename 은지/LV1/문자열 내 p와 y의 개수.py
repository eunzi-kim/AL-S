def solution(s):
    cnt_p = cnt_y = 0
    for x in s:
        if x == 'p' or x == 'P':
            cnt_p += 1
        elif x == 'y' or x == 'Y':
            cnt_y += 1
    if cnt_p == cnt_y:
        answer = True
    else:
        answer = False
    return answer