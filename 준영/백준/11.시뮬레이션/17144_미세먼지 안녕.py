import sys
input = sys.stdin.readline

R, C, T = map(int, input().split())

arr = []

for _ in range(R):
    arr.append(list(map(int, input().split())))

for m in range(C):
    if arr[m][0] == -1:
        up_care = m
        down_care = m+1
        break


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(T):
    # 미세먼지 확산
    temp = [[0 for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            
            sum_x = 0
            if arr[i][j] > 0:

                for k in range(4):
                    vi = i + dx[k]
                    vj = j + dy[k]

                    if vi < 0 or vj < 0 or vi >= R or vj >= C:
                        continue
                    
                    if vj == 0 and vi == up_care:
                        continue
                    elif vj == 0 and vi == down_care:
                        continue
                    else:
                        temp[vi][vj] += arr[i][j] // 5
                        sum_x += arr[i][j] // 5
                
            temp[i][j] -= sum_x

    for i in range(R):
        for j in range(C):
            arr[i][j] += temp[i][j]

    # 공기청정기 작동
    # 위
    for i in range(up_care-2, -1, -1):
        arr[i+1][0] = arr[i][0]
    
    for i in range(1, C):
        arr[0][i-1] = arr[0][i]

    for i in range(1, up_care+1):
        arr[i-1][C-1] = arr[i][C-1]

    for i in range(C-2, 0, -1):
        arr[up_care][i+1] = arr[up_care][i]

    arr[up_care][1] = 0

    #아래
    for i in range(down_care+2, R):
        arr[i-1][0] = arr[i][0]
    
    for i in range(1, C):
        arr[R-1][i-1] = arr[R-1][i]

    for i in range(R-2, down_care-1, -1):
        arr[i+1][C-1] = arr[i][C-1]

    for i in range(C-2, 0, -1):
        arr[down_care][i+1] = arr[down_care][i]
    
    arr[down_care][1] = 0

result = 0
for m in range(R):
    for n in range(C):
        result += arr[m][n]
result += 2
print(result)
