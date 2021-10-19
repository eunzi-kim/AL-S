import sys
input = sys.stdin.readline

N, X = map(int, input().split())
arr = list(map(int, input().split()))

# 누적합
arr_sum = [0]*(N+1)
for i in range(1, N+1):
    arr_sum[i] = arr[i-1]+arr_sum[i-1]
# print(arr_sum)

max_n = 0
cnt = 0

for i in range(X, N+1):
    sum_v = arr_sum[i]-arr_sum[i-X]
    if sum_v > max_n:
        max_n = sum_v
        cnt  = 1
    elif sum_v == max_n:
        cnt += 1

if max_n > 0:
    print(max_n)
    print(cnt)
else:
    print("SAD")