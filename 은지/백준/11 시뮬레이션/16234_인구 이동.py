import sys
input = sys.stdin.readline

N, L, R = map(int, input().split())
land = []
for _ in range(N):
    land.append(list(map(int, input().split())))

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def bfs(x, y):
    queue = [[x, y]]
    chain = [[x, y]]
    sum_chain = land[x][y]
    while queue:
        v = queue.pop(0)
        r = v[0]
        c = v[1]
        for i in range(4):
            new_r = r+dr[i]
            new_c = c+dc[i]
            if 0 <= new_r < N and 0 <= new_c < N and chk[new_r][new_c] == 0 and L <= abs(land[new_r][new_c]-land[r][c]) <= R:
                queue.append([new_r, new_c])
                chain.append([new_r, new_c])
                chk[new_r][new_c] = 1
                sum_chain += land[new_r][new_c]

    if len(chain) > 1:
        val = sum_chain // len(chain)
        for w in chain:
            land[w[0]][w[1]] = val
    return len(chain)

ans = 0
while True:
    open_cnt = 0
    chk = [[0] * N for _ in range(N)]
    for x in range(N):
        for y in range(N):
            if chk[x][y] == 0:
                chk[x][y] = 1
                v = bfs(x, y)
                if v > 1:
                    open_cnt = 1
    if open_cnt == 0:
        break
    ans += 1
print(ans)