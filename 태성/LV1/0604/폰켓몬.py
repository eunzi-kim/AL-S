def solution(nums):
    answer = 0
    set_nums = set(nums)
    if len(set_nums)>len(nums)/2:
        answer = len(nums)/2
    else:
        answer = len(set_nums)
    
    return answer