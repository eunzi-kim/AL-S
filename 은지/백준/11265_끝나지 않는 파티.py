import sys
input = sys.stdin.readline

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
       
for k in range(N):
    for i in range(N):
        for j in range(N):
            if board[i][j] > board[i][k]+board[k][j]:
                board[i][j] = board[i][k]+board[k][j]

for _ in range(M):
    A, B, C = map(int, input().split())
    if board[A-1][B-1] <= C:
        print("Enjoy other party")
    else:
        print("Stay here")