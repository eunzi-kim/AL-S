def solution(n):
    answer = 0
    s_n = str(n)
    # print(s_n)
    for s in s_n:
        answer += int(s)

    return answer