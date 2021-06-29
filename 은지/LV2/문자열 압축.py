def solution(s):
    n = len(s)
    answer = n
    # 문자열 자르기
    for x in range(1, n):
        exam = ''
        pre = ''
        cnt = 0
        for i in range(0, n, x):
            # 과거 문자열과 현재 문자열이 다른 경우
            if s[i:i+x] != pre:
                if cnt > 1:
                    exam += str(cnt) + pre
                else:
                    exam += pre
                pre = s[i:i+x]
                # 개수 초기화
                cnt = 1
                # 마지막 문자열
                if i >= n-x:
                    exam += pre
            # 과거 문자열과 현재 문자열이 같은 경우
            else:
                # 마지막 문자열
                if i >= n-x:
                    exam += str(cnt+1) + s[i:i+x]
                cnt += 1
        # 최소 문자열 탐색
        if answer > len(exam):
            answer = len(exam)
    return answer

s = "abcabcdede"
print(solution(s))