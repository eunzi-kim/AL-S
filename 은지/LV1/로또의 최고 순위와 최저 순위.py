def solution(lottos, win_nums):
    # 확실히 맞은 개수
    chk = 0
    # 0의 개수
    zero = 0
    for x in lottos:
        for y in win_nums:
            if x == y:
                chk += 1
        if x == 0:
            zero += 1
    # 0이 모두 맞지 않은 경우 => 최저 순위
    if chk >= 2:
        minR = 7 - chk
    else:
        minR = 6
    # 0이 모두 맞은 경우 => 최고 순위
    if (chk + zero) >= 2:
        maxR = 7 - (chk + zero)
    else:
        maxR = 6
    answer = [maxR, minR]
    return answer