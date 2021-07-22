def solution(number, k):
    answer = ''
    # 탐색 시작 위치 인덱스
    i = 0
    # 큰 수 만들어질때까지 반복
    while len(answer) < len(number)-k:
        # 가장 큰 한 자리수 탐색
        # i부터
        # len(number) - (len(nubmer)-k) + (구한 answer의 길이) 까지
        max_v = 0
        for j in range(i, k+1+len(answer)):
            # 가지치기
            # 9가 가장 큰 한 자리수이므로, 발견
            if int(number[j]) == 9:
                max_v = int(number[j])
                # 다음 탐색 첫 인덱스는 큰 수 다음
                i = j+1
                break
            # 가장 큰 수를 찾자
            if int(number[j]) > max_v:
                max_v = int(number[j])
                # 다음 탐색 첫 인덱스는 큰 수 다음
                i = j+1
        # 큰 수 넣기
        answer += str(max_v)
    return answer

n = "1231234"
k = 3
print(solution(n, k))