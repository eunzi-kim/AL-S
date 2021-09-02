import sys
input = sys.stdin.readline

N = int(input())

virus = [0 for _ in range(N+1)]

virus[1] = 1

graph_arr = [[0 for _ in range(N+1)] for _ in range(N+1)]

M = int(input())

for _ in range(M):
    x, y = map(int, input().split())

    graph_arr[x][y] = 1
    graph_arr[y][x] = 1

q = [1]

while q:
    x = q.pop(0)

    for i in range(1, N+1):
        if graph_arr[x][i] != 0 and virus[i] == 0:
            virus[i] = 1
            q.append(i)

print(sum(virus)-1)

