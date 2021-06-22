def solution(N, stages):
    answer = []
    # 실패율 리스트
    fail = []
    # 사용자수
    M = len(stages)
    for n in range(N):
        # 스테이지에 도달한 사람 수가 0인 경우
        if M == 0:
            fail.append(0)
        # 스테이지에 도달한 사람의 수가 0이 아닌 경우
        else:
            # 현재 단계에 있는 사람 수
            lv = stages.count(n+1)
            fail.append(lv/M)
            M -= lv
    # 스테이지 실패을 내림차순 정렬
    sort_fail = sorted(fail, reverse=True)
    # 목표 : 스테이지 실패율 많은 순서대로 answer에 추가
    Visited = [0] * N
    for i in range(N):
        for j in range(N):
            if Visited[j] == 0 and sort_fail[i] == fail[j]:
                Visited[j] = 1
                answer.append(j+1)
                break
    return answer