import sys
input = sys.stdin.readline

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    cost = int(input())

    dp = [0] * (cost+1)
    dp[0] = 1
    for x in arr:
        for i in range(x, cost+1):
            dp[i] += dp[i-x]
    
    print(dp[cost])