def solution(n):
    ans = 0
    # n이 0이면 끝!
    while n > 0:
        # 홀수이면 점프
        if n % 2:
            n -= 1
            ans += 1
        # 짝수이면 순간 이동
        else:
            n //= 2
    return ans