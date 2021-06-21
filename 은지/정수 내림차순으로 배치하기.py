def solution(n):
    # 정수 => 문자열 배열
    arr = []
    for x in str(n):
        arr.append(x)
    # 내림차순 정렬
    arr.sort(reverse=True)
    # 배열 => 문자열 => 정수
    answer = int("".join(arr))
    return answer