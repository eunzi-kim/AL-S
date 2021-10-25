import sys
input = sys.stdin.readline

N, X = map(int, input().split())
arr = list(map(int, input().split()))

x = sum(arr[:X])
result = x
cnt = 1
s_idx = 0
e_idx = X

for i in range(X, N):
    x -= arr[s_idx]
    x += arr[e_idx]

    if result < x:
        result = x
        cnt = 1
    elif result == x:
        cnt += 1

    s_idx += 1
    e_idx += 1

if result == 0:
    print('SAD')
else:
    print(result)
    print(cnt)