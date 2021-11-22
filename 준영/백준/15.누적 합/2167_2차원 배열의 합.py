import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

sum_arr = []
for i in range(N):
    temp = [0 for i in range(M)]
    add = 0
    for j in range(M-1, -1, -1):
        add += arr[i][j]
        temp[j] = add
    sum_arr.append(temp)

K = int(input())
result_arr = []
for _ in range(K):
    i, j, x, y = map(int, input().split())
    result = 0
    for ti in range(i-1, x):
        if y < M:
            result += sum_arr[ti][j-1] - sum_arr[ti][y]
        else:
            result += sum_arr[ti][j-1]

    result_arr.append(result)

for i in result_arr:
    print(i)