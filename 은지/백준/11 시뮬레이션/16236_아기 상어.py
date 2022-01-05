import sys
input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

pos = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            pos.append([i, j])
            board[i][j] = 0
            break
    if pos:
        break

time = 0
eat = 0
size = 2

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

while pos:
    x = pos.pop(0)
    queue = [[x[0], x[1], 0]]
    visited = [[0]*N for _ in range(N)]
    visited[x[0]][x[1]] = 1

    temp = []
    min_cnt = (N**N)+1

    while queue:
        v = queue.pop(0)
        r = v[0]
        c = v[1]
        cnt = v[2]

        for i in range(4):
            new_r = r+dr[i]
            new_c = c+dc[i]
            if 0 <= new_r < N and 0 <= new_c < N and visited[new_r][new_c] == 0 and board[new_r][new_c] <= size:
                visited[new_r][new_c] = 1
                queue.append([new_r, new_c, cnt+1])
                if 0 < board[new_r][new_c] < size and cnt+1 <= min_cnt:
                    min_cnt = cnt+1
                    temp.append([new_r, new_c, cnt+1])

    if temp:
        temp.sort()
        w = temp[0]

        time += w[2]
        eat += 1
        board[w[0]][w[1]] = 0

        if eat == size:
            eat = 0
            size += 1

        pos.append([w[0], w[1]])

print(time)