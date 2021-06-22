def two(x):
    if x < 2:
        return x
    else:
        return two(x//2) * 10 + x % 2

def solution(n, arr1, arr2):
    answer = []
    # 지도 초기화
    Map = [[0]*n for _ in range(n)]
    for i in range(n):
        # 10진수 => 2진수
        a1 = str(two(arr1[i]))
        a2 = str(two(arr2[i]))
        # 벽 입력
        for j in range(len(a1)-1, -1, -1):
            Map[i][j+n-len(a1)] += int(a1[j])
        for j in range(len(a2)-1, -1, -1):
            Map[i][j+n-len(a2)] += int(a2[j])
    # 지도 출력
    for i in range(n):
        result = ""
        for j in range(n):
            if Map[i][j]:
                result += "#"
            else:
                result += " "
        answer.append(result)
    return answer