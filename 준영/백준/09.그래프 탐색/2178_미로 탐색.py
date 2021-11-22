N, M = map(int, input().split())

arr = []

for i in range(N):
    arr.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visit = [[99999 for _ in range(M)] for _ in range(N)]

q = []

visit[0][0] = 1
q.append([1, 0, 0])

while q:
    dist, nowX, nowY = q.pop(0)

    for i in range(4):
        vx = nowX + dx[i]
        vy = nowY + dy[i]
        
        if vx < 0 or vy < 0 or vx >= N or vy >= M:
            continue

        if arr[vx][vy] == 0:
            continue

        if visit[vx][vy] > dist+1:
            q.append([dist+1, vx, vy])
            visit[vx][vy] = dist+1
        
print(visit[N-1][M-1])
