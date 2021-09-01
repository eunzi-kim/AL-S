import sys
input = sys.stdin.readline

N = int(input())

result = [[0 for _ in range(N)] for _ in range(N)]

like_arr = []

for _ in range(N*N):
    like_arr.append(list(map(int, input().split())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for k in range(N*N):
    temp = like_arr[k]
    q = []
    for i in range(N):
        for j in range(N):
            if result[i][j]:
                continue
            like = 0
            empty = 0
            for t in range(4):
                vx = i + dx[t]
                vy = j + dy[t]

                if vx < 0 or vx >= N or vy < 0 or vy >= N:
                    continue

                if result[vx][vy] == 0:
                    empty += 1

                if result[vx][vy] in temp[1:]:
                    like += 1

            q.append([i, j, like, empty])
    q.sort(key=lambda x:(-x[2], -x[3], x[0]))
    x, y, like_t, empty_t = q[0]
    result[x][y] = temp[0]

like_arr.sort(key=lambda x:x[0])

final_result = 0

for i in range(N):
    for j in range(N):
        temp = 0
        for t in range(4):
            vx = i + dx[t]
            vy = j + dy[t]

            if vx < 0 or vx >= N or vy < 0 or vy >= N:
                continue
            
            if result[vx][vy] in like_arr[result[i][j]-1][1:]:
                temp += 1

        final_result += int(10**(temp-1))
            

print(final_result)

