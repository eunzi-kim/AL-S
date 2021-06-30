def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    # 기능별 걸리는 시간
    day = [0]*n
    for i in range(n):
        # 남은 작업량
        r = 100 - progresses[i]
        # 필요한 시간
        d = 0
        while r > 0:
            r -= speeds[i]
            d += 1
        day[i] = d
    # 작업 수 구하기
    i = 0  # day 인덱스
    cnt = 1  # 배포할 작업 개수
    pre = day[0]  # 배포 시작 (기준)
    while i < n:
        # 다음 작업도 배포 가능
        if i < n-1 and pre >= day[i+1]:
            cnt += 1
            i += 1
        # 다음 작업 배포 불가능
        else:
            answer.append(cnt)
            if i < n-1:
                pre = day[i+1]
            cnt = 1
            i += 1
    return answer

p = [93, 30, 55, 60, 40, 65]
s = [1, 30, 5 , 10, 60, 7]
print(solution(p, s))