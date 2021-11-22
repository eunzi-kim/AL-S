import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]
clouds = [[N-1, 0], [N-1, 1], [N-2, 0], [N-2, 1]]

c_dr = [-1, -1, 1, 1]
c_dc = [-1, 1, -1, 1]

for _ in range(M):
    d, s = map(int, input().split())
    temp_clouds = []

    # 1. 비내리기
    visited = [[0]*N for _ in range(N)]

    for cloud in clouds:
        r = cloud[0]
        c = cloud[1]
        new_r = (r+(dr[d]*s))%N
        new_c = (c+(dc[d]*s))%N
        board[new_r][new_c] += 1
        temp_clouds.append([new_r, new_c])

        visited[new_r][new_c] = 1

    # 2. 물복사버그
    for temp_cloud in temp_clouds:
        r = temp_cloud[0]
        c = temp_cloud[1]
        for j in range(4):
            cross_r = r + c_dr[j]
            cross_c = c + c_dc[j]
            if 0 <= cross_r < N and 0 <= cross_c < N and board[cross_r][cross_c]:
                board[r][c] += 1

    # 3. 구름 생성
    clouds = []
    for r in range(N):
        for c in range(N):
            if board[r][c] >= 2 and visited[r][c] == 0:  # not in 이용해서 계속 시간초과 생김!
                board[r][c] -= 2
                clouds.append([r, c])

ans = 0
for r in range(N):
    for c in range(N):
        ans += board[r][c]

print(ans)