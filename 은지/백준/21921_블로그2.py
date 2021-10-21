N, X = map(int, input().split())
arr = list(map(int, input().split()))

max_v = sum(arr[:X])
cnt = 1

temp_sum = max_v
for i in range(N-X):
    temp_sum = temp_sum - arr[i] + arr[i+X]
    if temp_sum > max_v:
        max_v = temp_sum
        cnt = 1
    elif temp_sum == max_v:
        cnt += 1

if max_v:
    print(max_v)
    print(cnt)
else:
    print("SAD")