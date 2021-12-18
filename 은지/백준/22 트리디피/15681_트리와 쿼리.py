import sys
input = sys.stdin.readline

N, R, Q = map(int, input().split())

g = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

child = [[] for _ in range(N+1)]

visited = [0] * (N+1)

queue = [R]
visited[R] = 1
while queue:
    x = queue.pop(0)
    for w in g[x]:
        if visited[w] == 0:
            visited[w] = 1
            child[x].append(w)
            queue.append(w)

# print(child)

for _ in range(Q):
    u = int(input())

    cnt = 0

    queue = [u]
    while queue:
        x = queue.pop(0)
        cnt += 1
        for w in child[x]:
            queue.append(w)

    print(cnt)