def solution(n):
    answer = []
    s_n = str(n)
    for i in range(len(s_n)-1, -1, -1):
        answer.append(int(s_n[i]))
    return answer