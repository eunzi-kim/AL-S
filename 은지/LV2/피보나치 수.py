def fibo(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return solution(x-1) + solution(x-2)

def solution(n):
    return fibo(n) % 1234567


###############################################


def solution(n):
    a = 0
    b = 1
    for _ in range(n-1):
        c = a + b
        a = b
        b = c
    answer = b % 1234567
    return answer