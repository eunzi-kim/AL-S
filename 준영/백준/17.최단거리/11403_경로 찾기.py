import sys
input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

result_arr = []

for i in range(N):
    result = [0 for _ in range(N)]
    q = []
    for j in range(N):
        if arr[i][j]:
            q.append(j)
    while q:
        x = q.pop(0)
        result[x] = 1
        for k in range(N):
            if arr[x][k] and result[k] == 0:
                q.append(k)
    result_arr.append(result)

for i in range(N):
    print(*result_arr[i])