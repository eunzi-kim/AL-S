def solution(num):
    answer = 0
    while num != 1:
        # 짝수
        if num % 2 == 0:
            num //= 2
        # 홀수
        else:
            num = num * 3 + 1
        answer += 1
        # 500번 초과 반복
        if answer > 500:
            answer = -1
            break
    return answer