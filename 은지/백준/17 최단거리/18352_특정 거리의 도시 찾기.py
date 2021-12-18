import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

g = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    g[A].append(B)

dis = [9999999999] * (N+1)
queue = [X]
dis[X] = 0
while queue:
    v = queue.pop(0)
    for w in g[v]:
        if dis[v]+1 < dis[w] and dis[v]+1 <= K:  # K보다 긴 거리는 생각하지 말자벌레
            dis[w] = dis[v]+1
            queue.append(w)

ans = []
for i in range(1, N+1):
    if dis[i] == K:
        ans.append(i)

if len(ans):
    for x in ans:
        print(x)
else:
    print(-1)