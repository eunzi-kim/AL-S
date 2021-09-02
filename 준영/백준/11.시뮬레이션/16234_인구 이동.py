import sys, math
input = sys.stdin.readline

N, L, R = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(list(map(int, input().split())))

result = -1

q = []

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
change = True
while change:
    result += 1
    change = False
    temp = [[0 for _ in range(N)] for _ in range(N)]
    idx = 0
    
    change_days = []

    for i in range(N):
        for j in range(N):
            idx += 1
            if temp[i][j] == 0:
                q = [[i, j]]
                temp[i][j] = idx

            noline = [[i, j]]

            while q:

                x, y = q.pop(0)

                for t in range(4):
                    vx = x + dx[t]
                    vy = y + dy[t]

                    if vx < 0 or vx >= N or vy < 0 or vy >= N:
                        continue

                    if temp[vx][vy]:
                        continue
                    
                    if abs(arr[vx][vy] - arr[x][y]) >= L and abs(arr[vx][vy] - arr[x][y]) <= R:
                        q.append([vx, vy])
                        temp[vx][vy] = idx
                        noline.append([vx, vy])

            if len(noline) > 1:
                change_days.append(noline)

    for i in change_days:
        change = True
        sum_a = 0
        len_a = len(i)

        for j in i:
            sum_a += arr[j[0]][j[1]]
        
        for j in i:
            arr[j[0]][j[1]] = math.floor(sum_a / len_a)

print(result)

