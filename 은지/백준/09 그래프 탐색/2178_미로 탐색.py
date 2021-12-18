N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

queue = [[0, 0]]
while queue:
    v = queue.pop(0)
    r = v[0]
    c = v[1]

    for i in range(4):
        new_r = r+dr[i]
        new_c = c+dc[i]
        if 0 <= new_r < N and 0 <= new_c < M and board[new_r][new_c] == '1':
            queue.append([new_r, new_c])
            board[new_r][new_c] = int(board[r][c]) + 1

print(board[N-1][M-1])