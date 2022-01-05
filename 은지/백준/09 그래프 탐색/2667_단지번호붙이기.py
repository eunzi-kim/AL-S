N = int(input())
board = [list(input()) for _ in range(N)]

visited = [[0]*N for _ in range(N)]


def search(i, j):
    cnt = 1
    visited[i][j] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    queue = [[i, j]]
    while queue:
        v = queue.pop(0)
        r = v[0]
        c = v[1]

        for k in range(4):
            new_r = r+dr[k]
            new_c = c+dc[k]
            if 0 <= new_r < N and 0 <= new_c < N and board[new_r][new_c] == "1" and visited[new_r][new_c] == 0:
                visited[new_r][new_c] = 1
                queue.append([new_r, new_c])
                cnt += 1

    return cnt
    

ans = []

for i in range(N):
    for j in range(N):
        if visited[i][j] == 0 and board[i][j] == "1":
            ans.append(search(i, j))

print(len(ans))
ans.sort()
for x in ans:
    print(x)