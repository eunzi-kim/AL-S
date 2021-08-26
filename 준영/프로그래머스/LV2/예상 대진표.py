def solution(n,a,b):
    answer = 1
    # a_seed = (a // 2) + 1 if a % 2 else a // 2
    a_seed = (a // 2) + (a % 2)
    b_seed = (b // 2) + 1 if b % 2 else b // 2
    
    while n != 1:
        if a_seed == b_seed:
            break

        a_seed = (a_seed // 2) + 1 if a_seed % 2 else a_seed // 2
        b_seed = (b_seed // 2) + 1 if b_seed % 2 else b_seed // 2
        
        answer += 1
        n //= 2
    return answer

solution(8,4,7)
print(solution(8, 4, 7))