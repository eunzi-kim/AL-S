T = int(input())
for _ in range(T):
    ans = 1
    N, M = map(int, input().split())
    if N == 0:
        print(0)
    else:
        for i in range(N):
            ans *= (M-i)
        for i in range(1, N+1):
            ans //= i
        print(ans)