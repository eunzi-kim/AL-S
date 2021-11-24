import sys
input = sys.stdin.readline
from copy import deepcopy

R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

air = []
for r in range(R):
    if board[r][0] == -1:
        air.append(r)

for _ in range(T):
    # 미세먼지 확산
    temp = [[0]*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if board[r][c] > 0:
                cnt = 0
                for i in range(4):
                    new_r = r+dr[i]
                    new_c = c+dc[i]
                    if 0 <= new_r < R and 0 <= new_c < C and board[new_r][new_c] != -1:
                        cnt += 1
                        temp[new_r][new_c] += board[r][c] // 5
                temp[r][c] += board[r][c] - ((board[r][c]//5)*cnt)

    board = deepcopy(temp)
    board[air[0]][0] = -1
    board[air[1]][0] = -1

    # 위쪽 공기청정기 작동
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]
    r = air[0]
    c = 1
    i = 0
    pre = 0
    while True:
        temp = board[r][c]
        board[r][c] = pre
        pre = temp
        
        new_r = r+dr[i]
        new_c = c+dc[i]
        if new_r == air[0] and new_c == 0:
            break
        elif 0 <= new_r < R and 0 <= new_c < C:
            r = new_r
            c = new_c        
        else:
            i += 1
            r = r+dr[i]
            c = c+dc[i]

    # 아래쪽 공기청정기 작동
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    r = air[1]
    c = 1
    i = 0
    pre = 0
    while True:
        temp = board[r][c]
        board[r][c] = pre
        pre = temp
        
        new_r = r+dr[i]
        new_c = c+dc[i]
        if new_r == air[1] and new_c == 0:
            break
        elif 0 <= new_r < R and 0 <= new_c < C:
            r = new_r
            c = new_c        
        else:
            i += 1
            r = r+dr[i]
            c = c+dc[i]

ans = 2
for r in range(R):
    for c in range(C):
        ans += board[r][c]
print(ans)