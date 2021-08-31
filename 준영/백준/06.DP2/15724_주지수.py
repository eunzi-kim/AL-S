import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [[0 for _ in range(M+1)]]

for _ in range(N):
    arr.append([0] + list(map(int, input().split())))

for i in range(N+1):
    for j in range(2, M+1):
        arr[i][j] += arr[i][j-1]

for i in range(M+1):
    for j in range(2, N+1):
        arr[j][i] += arr[j-1][i]
        
K = int(input())

for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    print(arr[x2][y2] - arr[x1-1][y2] - arr[x2][y1-1] + arr[x1-1][y1-1])

