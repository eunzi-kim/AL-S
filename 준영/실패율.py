def solution(N, stages):
    answer = []
    arr = [[0, 0, i]for i in range(N)]

    for i in stages:
        for j in range(0, i-1):
            arr[j][0] += 1
            
    div = len(stages)

    for i in range(N):
        if div == 0:
            arr[i][1] = 0
        else:
            arr[i][1] = (div - arr[i][0]) / div
        div = arr[i][0]

    arr.sort(key=lambda x: (-x[1]))

    for i in range(N):
        answer.append(arr[i][2]+1)
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
