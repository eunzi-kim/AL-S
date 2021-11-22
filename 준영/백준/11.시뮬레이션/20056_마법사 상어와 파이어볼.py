import copy
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

arr = [[[] for _ in range(N)] for _ in range(N)]

for i in range(M):
    r, c, m, s, d = map(int, input().split())
    arr[r-1][c-1].append((m, s, d, 1))

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    two_fire_ball = []
    temp_arr = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j]:
                for k in arr[i][j]:
                    m, s, d, n = k
                    dx = i+dr[d]*s
                    dy = j+dc[d]*s
                    while dx >= N:
                        dx = dx - N
                    while dy >= N:
                        dy = dy - N

                    if temp_arr[dx][dy]:
                        tm, ts, td, n = temp_arr[dx][dy][0]
                        temp_arr[dx][dy] = [(tm+m, ts+s, td+d, n+1)]
                        two_fire_ball.append((dx, dy))
                    else:
                        temp_arr[dx][dy] = [(m, s, d, 1)]

    for i, j in two_fire_ball:
        m, s, d, n = temp_arr[i][j][0]
        m = m//5
        s = s//n
        dx = [1, 3, 5, 7]
        dy = [0, 2, 4, 6]
        temp = []
        if m != 0:
            for k in range(4):
                if d % 2:
                    temp.append((m, s, dx[k], 1))
                else:
                    temp.append((m, s, dy[k], 1))
        temp_arr[i][j] = copy.deepcopy(temp)

    arr = copy.deepcopy(temp_arr)

result = 0

for i in range(N):
    for j in range(N):
        for k in arr[i][j]:
            m, s, d, n = k
            result += m
print(arr)
print(result)