import sys
input = sys.stdin.readline

N, M = map(int, input().split())
info = [[0]*(M+1)] + [[0]+list(map(int, input().split())) for _ in range(N)]

for r in range(1, N+1):
    for c in range(1, M+1):
        info[r][c] += info[r][c-1]

for r in range(1, N+1):
    for c in range(1, M+1):
        info[r][c] += info[r-1][c]

K = int(input())
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    print(info[x2][y2] - info[x1-1][y2] - info[x2][y1-1] + info[x1-1][y1-1])
