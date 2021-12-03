import sys
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))

Q = int(input())

temp = [0 for _ in range(N+1)]

temp_sum = 0
for i in range(N-1):
    if arr[i] > arr[i+1]:
        temp_sum += 1
    temp[i+1] = temp_sum
temp[N] = temp_sum

for i in range(Q):
    x, y = map(int, input().split())

    print(temp[y-1] - temp[x-1])