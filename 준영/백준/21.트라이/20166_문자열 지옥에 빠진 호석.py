N, M, K = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(input()))

result_dict = {}

def dfs(x, y, t, n):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    
    if result_dict.get(t):
        result_dict[t] += 1
    else:
        result_dict[t] = 1

    if n <= 5:
        for i in range(8):
            vx = x + dx[i]
            vy = y + dy[i]
            
            if vx < 0:
                vx = N - 1
            if vy < 0:
                vy = M - 1

            if vx >= N:
                vx = 0
            if vy >= M:
                vy = 0
            dfs(vx, vy, t + arr[vx][vy], n+1)

for i in range(N):
    for j in range(M):
        dfs(i, j, arr[i][j], 1)


for i in range(K):
    temp = input()
    if result_dict.get(temp):
        print(result_dict[temp])
    else:
        print(0)