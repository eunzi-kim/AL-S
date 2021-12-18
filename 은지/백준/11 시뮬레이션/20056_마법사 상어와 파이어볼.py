N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

ball = []

for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    new_r = (r-1)+(dr[d]*s)
    new_c = (c-1)+(dc[d]*s)

    if 0 <= new_r < N and 0 <= new_c < N:
        board[new_r][new_c].append([m, s, d%2])
        if (new_r, new_c) not in ball:
            ball.append((new_r, new_c))

while ball:
    x = ball.pop(0)
    r = x[0]
    c = x[1]

    if len(board[r][c]) >= 2:
        fat = speed = 0
        pre = -1
        chk = True
        for v in board[r][c]:
            fat += v[0]
            speed += v[1]
            if pre == -1:
                pre = v[2]
            elif pre != v[2]:
                chk = False
            else:
                pre = v[2]
        fat = fat // 5
        speed = speed//len(board[r][c])

        board[r][c] = []

        if chk:
            for i in range(0, 7, 2):
                board[r+dr[i]][c+dc[i]].append([fat, speed, 0])
                if (r+dr[i], c+dc[i]) not in ball:
                    ball.append((r+dr[i], c+dc[i]))
        else:
            for i in range(1, 8, 2):        
                board[r+dr[i]][c+dc[i]].append([fat, speed, 1])
                if (r+dr[i], c+dc[i]) not in ball:
                    ball.append((r+dr[i], c+dc[i]))

ans = 0
for r in range(N):
    for c in range(N):
        if board[r][c]:
            ans += board[r][c][0][0]

print(ans)
        



# 4 2 1
# 1 1 5 2 2
# 1 4 7 1 6
# r c m s d

# 8