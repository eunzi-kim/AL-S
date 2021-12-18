N, M, K = map(int, input().split())
board = [list(input()) for _ in range(N)]

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

for _ in range(K):
    cnt = 0
    s = input()
    queue = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == s[0]:
                queue.append([i, j, s[1:]])

    while queue:
        v = queue.pop(0)
        r = v[0]
        c = v[1]
        s = v[2]

        if len(s) == 0:
            cnt += 1
        
        elif r == 0 or c == 0 or r == N-1 or c == M-1:
            x = s[0]
            for i in range(N):
                if board[i][0] == x and (r != i or c != 0):
                    queue.append([i, 0, s[1:]])
                if board[i][M-1] == x and (r != i or c != M-1):
                    queue.append([i, M-1, s[1:]])  

            for i in range(1, M-1):
                if board[0][i] == x and (r != 0 or c != i):
                    queue.append([0, i, s[1:]])
                if board[N-1][i] == x and (r != N-1 or c != i):
                    queue.append([N-1, i, s[1:]])

            for i in range(8):
                new_r = r+dr[i]
                new_c = c+dc[i]
                if 0 < new_r < N-1 and 0 < new_c < M-1 and board[new_r][new_c] == x:
                    queue.append([new_r, new_c, s[1:]])
        
        else:
            x = s[0]
            for i in range(8):
                new_r = r+dr[i]
                new_c = c+dc[i]
                if board[new_r][new_c] == x:
                    queue.append([new_r, new_c, s[1:]])
                
    print(cnt)