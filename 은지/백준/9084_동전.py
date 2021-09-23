T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    M = int(input())

    dp = [0] * (M+1)  # 각 인덱스 => 만들어야 하는 금액
    dp[0] = 1
    for x in arr:
        for i in range(x, M+1):
            dp[i] += dp[i-x]
    
    print(dp[M])
