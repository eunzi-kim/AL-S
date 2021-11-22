import sys
input = sys.stdin.readline

str_1 = input().rstrip()
str_2 = input().rstrip()

n = len(str_1)
m = len(str_2)

dp = [[0]*(n+1) for _ in range(m+1)]

for j in range(1, m+1):
    for i in range(1, n+1):
        if str_1[i-1] == str_2[j-1]:
            dp[j][i] = dp[j-1][i-1]+1
        else:
            dp[j][i] = max(dp[j-1][i], dp[j][i-1])

print(dp[m][n])