N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort(reverse=True)

ans = 0
for i in range(N):
    if arr[i]-i > 0:
        ans += arr[i]-i

print(ans)