### 다시 풀기!! ###

import sys
input = sys.stdin.readline

N = int(input())

pos = [[0]*N for _ in range(N)]
like_f = [[] for _ in range(N**2+1)]

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

for _ in range(N**2):
    info = list(map(int, input().split()))
    x = info[0]
    like_f[x] = info[1:]

    for r in range(N):
        for c in range(N):
            if pos[r][c] == 0:
                tmp = 0
                for k in range(4):
                    if pos[r+dr[k]][c+dc[k]] in like_f[x]:
                        tmp += 1

print(like_f)