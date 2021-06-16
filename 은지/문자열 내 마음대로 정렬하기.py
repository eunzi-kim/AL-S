def solution(strings, n):
    # 문자열 맨 앞에 n번째 글자 입력
    for i in range(len(strings)):
        strings[i] = strings[i][n] + strings[i]
    # 정렬
    strings.sort()
    # 문자열에 추가했던 n번째 글자 제거
    for i in range(len(strings)):
        strings[i] = strings[i][1:]
    return strings