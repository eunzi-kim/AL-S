def solution(n, lost, reserve):
    Cloth = [1] * (n+1)
    # 여벌의 체육복 입력
    for x in reserve:
        Cloth[x] += 1
    # 도난 체육복 입력
    for x in lost:
        Cloth[x] -= 1
    # 체육복 check!
    for i in range(1, n+1):
        # i번째 학생이 체육복이 없음
        if Cloth[i] < 1:
            if i-1 > 0 and Cloth[i-1] > 1:
                Cloth[i] += 1
                Cloth[i-1] -= 1
            elif i+1 <= n and Cloth[i+1] > 1:
                Cloth[i] += 1
                Cloth[i+1] -= 1
    # 결과값 초기화
    answer = -1
    for x in Cloth:
        if x > 0:
            answer += 1
    return answer