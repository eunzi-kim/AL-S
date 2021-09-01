def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def solution(w,h):
    gcd_cal = gcd(w, h)
    answer = w * h - w - h + gcd_cal
    return answer