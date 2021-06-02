def solution(answers):
    answer = []
    # 문제의 개수
    N = len(answers)
    # A의 답안
    A = [x%5+1 for x in range(N)]
    # B의 답안
    B = []
    b = [1, 3, 4, 5]
    for i in range(N//2+1):
        B.append(2)
        B.append(b[i%4])
    # C의 답안
    C = []
    c = [3, 1, 2, 4, 5]
    for i in range(N//2+1):
        C.append(c[i%5])
        C.append(c[i%5])
    # 답 체크
    Check = [0, 0, 0]
    for i in range(N):
        if A[i] == answers[i]:
            Check[0] += 1
        if B[i] == answers[i]:
            Check[1] += 1
        if C[i] == answers[i]:
            Check[2] += 1
    # 가장 높은 점수
    maxV = max(Check)
    # 가장 높은 점수 학생 탐색
    for i in range(3):
        if Check[i] == maxV:
            answer.append(i+1)
    return answer