from itertools import combinations

def is_prime(num):
    i = 2
    while i < num:
        if num % i == 0:
            return False
        i += 1
    return True 

def solution(nums):
    answer = 0
    nums.sort()

    comb_list = list(combinations(nums, 3))

    for i in comb_list:
        if is_prime(sum(i)):
            answer += 1
    
    return answer

nums = [1, 2, 3, 4]
print(solution(nums))