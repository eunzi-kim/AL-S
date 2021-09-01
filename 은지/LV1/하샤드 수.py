def solution(x):
    answer = True
    # 자릿수 합
    y = x
    v = 0
    while y > 0:
        v += y % 10
        y //= 10
    # 조건
    if x % v:
        answer = False    
    return answer