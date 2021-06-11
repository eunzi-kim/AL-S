# 약수의 개수 구하는 함수
def div(a):
    cnt = 0
    for b in range(1, a+1):
        if a % b == 0:
            cnt += 1
    return cnt

def solution(left, right):
    answer = 0
    for x in range(left, right+1):
        # x의 약수의 개수
        n = div(x)
        # 약수의 개수가 홀수
        if n % 2:
            answer -= x
        # 약수의 개수가 짝수
        else:
            answer += x
    return answer