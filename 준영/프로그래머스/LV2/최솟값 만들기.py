def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse=True)
    
    N = len(A)

    for i in range(N):
        answer += (A[i] * B[i])

    return answer