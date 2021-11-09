N = int(input())

arr = [0] + list(map(int, input().split()))

tree = [[] for i in range(N+1)]

for i in range(N-1):
    x, y = map(int, input().split())

    tree[x].append(y)
    tree[y].append(x)

dp = [[0, 0] for _ in range(N+1)]
dp_idx = [[[i], []] for i in range(N+1)]
visit = [True for _ in range(N+1)]

def dfs(now):
    visit[now] = False
    dp[now][0] = arr[now]
    dp[now][1] = 0

    for i in tree[now]:
        if visit[i]:
            dfs(i)
            dp[now][0] += dp[i][1]
            dp_idx[now][0].extend(dp_idx[i][1])
            
            dp[now][1] += max(dp[i][0], dp[i][1])
            if dp[i][0] > dp[i][1]:
                dp_idx[now][1].extend(dp_idx[i][0])
            else:
                dp_idx[now][1].extend(dp_idx[i][1])

            

dfs(1)
print(dp_idx)
print(dp)
print(max(dp[1][0], dp[1][1]))
if dp[1][0] > dp[1][1]:
    print(*(sorted(dp_idx[1][0])))
else:
    print(*(sorted(dp_idx[1][1])))

    