import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
arr = [[0]*(N+1) for _ in range(N+1)]

for i in range(N):
    for j in range(N):
        if i == 0 and j == 0:
            arr[i+1][j+1] = board[i][j]
        elif i == 0:
            arr[i+1][j+1] = arr[i+1][j] + board[i][j]
        elif j == 0:
            arr[i+1][j+1] = arr[i][j+1] + board[i][j]
        else:
            arr[i+1][j+1] = arr[i][j+1] + arr[i+1][j] + board[i][j] - arr[i][j]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(arr[x2][y2]-arr[x1-1][y2]-arr[x2][y1-1]+arr[x1-1][y1-1])