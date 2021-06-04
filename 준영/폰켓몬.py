def solution(nums):
    answer = 0
    n = len(nums)
    nums = list(set(nums))
    m = len(nums)

    if n // 2 < m:
        answer = n // 2
    else:
        answer = m
    
    return answer

nums = [3,1,2,3]
print(solution(nums))
nums = [3,3,3,2,2,4]
print(solution(nums))
nums = [3,3,3,2,2,2]
print(solution(nums))
