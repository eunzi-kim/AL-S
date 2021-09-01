def solution(x):
    answer = False
    temp = x
    hasyad = 0
    while temp:
        hasyad += (temp % 10)
        temp //= 10
    if x % hasyad == 0:
        answer = True
    return answer