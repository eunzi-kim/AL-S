def solution(n):
    answer = 0
    for i in range(1, n+1):
        temp = i
        sum_a = i
        while sum_a < n:
            temp += 1
            sum_a += temp
        if sum_a == n:
            answer += 1
    
    return answer

solution(15)