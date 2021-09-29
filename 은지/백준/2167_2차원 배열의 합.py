N, M = map(int, input().split())
arr = [[0]*(M+1)]
for _ in range(N):
    temp = [0] + list(map(int, input().split()))
    for i in range(2, M+1):
        temp[i] += temp[i-1]
    arr.append(temp)

for c in range(M+1):
    for r in range(2, N+1):
        arr[r][c] += arr[r-1][c]

K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    print(arr[x][y]-arr[x][j-1]-arr[i-1][y]+arr[i-1][j-1])