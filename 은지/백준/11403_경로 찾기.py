N = int(input())
g = [[] for _ in range(N)]

for i in range(N):
    arr = list(map(int, input().split()))
    for j in range(N):
        if arr[j]:
            g[i].append(j)

temp = [[] for _ in range(N)]

for i in range(N):
    queue = [i]
    while queue:
        v = queue.pop(0)        
        for w in g[v]:
            if w not in temp[i]:
                queue.append(w)
                temp[i].append(w)

for r in range(N):
    ans = [0]*N
    for x in temp[r]:
        ans[x] = 1
    print(*ans)