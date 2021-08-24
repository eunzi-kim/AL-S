def solution(n):
    answer = 0
    fibo = [0, 1]
    for i in range(n-1):
        fibo.append(fibo[-1] + fibo[-2])
    answer = fibo[-1] % 1234567
    return answer

solution(3)
solution(100)