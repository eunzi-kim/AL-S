def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def solution(n, m):
    gcd_temp = gcd(n, m)
    lcm_temp = (n * m) // gcd_temp
    answer = [gcd_temp, lcm_temp]
    return answer
