import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

g = [[] for _ in range(n+1)]
for _ in range(n-1):
    s, e = map(int, input().split())
    g[s].append(e)
    g[e].append(s)

dp = [[0, i] for i in range(n+1)]
link_arr = [[] for _ in range(n+1)]

for i in range(1, n+1):
    queue = [[[i], arr[i-1]]]
    while queue:
        x = queue.pop(0)
        link = x[0]
        w = x[1]
        v = link[-1]

        if w > dp[i][0]:
            dp[i][0] = w
            link_arr[i] = link

        for j in range(v+1, n+1):
            for x in link:
                if x in g[j]:
                    break
            else:
                temp = link + [j]
                queue.append([temp, w+arr[j-1]])

dp.sort(reverse=True)
print(dp[0][0])
x = dp[0][1]
print(*link_arr[x])
