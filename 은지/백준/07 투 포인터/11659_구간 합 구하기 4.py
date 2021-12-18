import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 누적합 배열
sum_arr = [0] * N
for i in range(len(arr)):
    sum_arr[i] = sum_arr[i-1] + arr[i]
# print(sum_arr)

for _ in range(M):
    i, j =  map(int, input().split())

    if i > 1:
        print(sum_arr[j-1]-sum_arr[i-2])
    else:
        print(sum_arr[j-1])