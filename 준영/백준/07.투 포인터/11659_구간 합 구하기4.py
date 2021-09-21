import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = [0] * N

temp = 0
for i in range(N-1, -1, -1):
    temp += arr[i]
    sum_arr[i] = temp
    
result = []
for _ in range(M):
    x, y = map(int, input().split())
    if y == N:
        result.append(sum_arr[x-1])
    else:
        result.append(sum_arr[x-1] - sum_arr[y])

print(' '.join(map(str, result)))