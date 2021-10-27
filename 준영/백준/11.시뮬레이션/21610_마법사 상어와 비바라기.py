import sys, copy
input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

raindrop = [[0 for _ in range(N)] for _ in range(N)]

def magic(d, s, n):
    global raindrop
    
    dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
    dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]

    temp = [[0 for _ in range(N)] for _ in range(N)]
    
    if n == 0:
        for i in range(2):
            for j in range(2):
                vx = (N -2 + i) + dx[d] * s
                vy = j + dy[d] * s

                while vx >= N or vx < 0:
                    if vx >= N:
                        vx = N - vx
                    elif vx < 0:
                        vx = N + vx

                while vy >= N or vy < 0:
                    if vy >= N:
                        vy = N - vy
                    elif vy < 0:
                        vy = N + vy
                        
                temp[vx][vy] = 1
    else:
        for i in range(N):
            for j in range(N):
                if arr[i][j] >= 2 and raindrop[i][j] != 1:
                    arr[i][j] -= 2
                    vx = (N -2 + i) + dx[d] * s
                    vy = j + dy[d] * s

                    while vx >= N or vx < 0:
                        if vx >= N:
                            vx = N - vx
                        elif vx < 0:
                            vx = N + vx

                    while vy >= N or vy < 0:
                        if vy >= N:
                            vy = N - vy
                        elif vy < 0:
                            vy = N + vy

                    temp[vx][vy] += 1
        
    for i in range(N):
        for j in range(N):
            if temp[i][j] == 1:
                arr[i][j] += 1

    raindrop = copy.deepcopy(temp)

    for i in range(N):
        for j in range(N):
            if temp[i][j] == 1:
                sum_x = 0

                if i - 1 >= 0:
                    if j - 1 >= 0:
                        if arr[i-1][j-1] >= 1:
                            sum_x += 1
                    
                    if j + 1 < N:
                        if arr[i-1][j+1] >= 1:
                            sum_x += 1

                if i + 1 < N:
                    if j - 1 >= 0:
                        if arr[i+1][j-1] >= 1:
                            sum_x += 1
                    
                    if j + 1 < N:
                        if arr[i+1][j+1] >= 1:
                            sum_x += 1
                
                arr[i][j] += sum_x
                    


for i in range(M):
    d, s = map(int, input().split())

    magic(d, s, i)

print(arr)
