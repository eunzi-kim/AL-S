T = int(input())
for i in range(1, T+1):
    N, M = map(int, input().split())
    x = 1
    for i in range(M, M-N, -1):
        x *= i
    y = 1
    for i in range(1, N+1):
        y *= i
    print(x//y)
