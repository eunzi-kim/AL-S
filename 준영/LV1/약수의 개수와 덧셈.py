def div(n):
    idx = 1
    cnt = 0
    while idx <= n:
        if n % idx == 0:
            cnt += 1
        idx += 1
    return cnt
        

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if div(i) % 2:
            answer -= i
        else:
            answer += i
            
    return answer