import math

def solution(w,h):
    # 최대공약수
    g = math.gcd(w, h)
    answer = (w * h) - (g * (w//g + h//g - 1))    
    return answer