def solution(lottos, win_nums):
    answer = []
    dic = {
        0:6,
        2:5,
        3:4,
        4:3,
        5:2,
        6:1,
    }
    max_cnt = 0
    for l in lottos:
        if l == 0:
            max_cnt += 1
        else:
            for w in win_nums:
                if l == w:
                    max_cnt += 1

    if max_cnt == 0 or max_cnt == 1:
        max_cnt = 0
    answer.append(dic[max_cnt])
    
    min_cnt = 0
    for l in lottos:
        for w in win_nums:
            if l == w:
                min_cnt += 1

    if min_cnt == 0 or min_cnt == 1:
        min_cnt = 0

    answer.append(dic[min_cnt])
    return answer