N, K = map(int, input().split())

dp = [[0]*201 for _ in range(201)]

for i in range(201):
    for j in range(201):
        if i == 0:
            dp[i][j] = 1
        elif j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(dp[K-1][N]%1000000000)