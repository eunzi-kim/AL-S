def solution(lottos, win_nums):
    answer = []
    zero_nums = lottos.count(0)
    result = 0
    for i in lottos:
        if i in win_nums:
            result += 1
    if 7-(result+zero_nums) > 6:
        best_win = 6
    else:
        best_win = 7-(result+zero_nums)
    
    if 7-result > 6:
        worst_win = 6
    else:
        worst_win = 7-result

    answer.append(best_win)
    answer.append(worst_win)

    return answer


lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))
lottos = [0, 0, 0, 0, 0, 0]	
win_nums = [38, 19, 20, 40, 15, 25]
print(solution(lottos, win_nums))
lottos = [45, 4, 35, 20, 3, 9]	
win_nums = [20, 9, 3, 45, 4, 35]	
print(solution(lottos, win_nums))
