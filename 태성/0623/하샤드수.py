def solution(x):
    answer = True
    x_s = str(x)

    pre = 0
    for a in x_s:
        pre += int(a)

    if x / pre == int(x / pre):
        answer = True
    else:
        answer = False
    return answer