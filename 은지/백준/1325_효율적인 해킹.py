import sys
input = sys.stdin.readline
from collections import deque

N, M = map(int, input().split())

g = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    g[B].append(A)

ans = set()
max_n = 0

for i in range(1, N+1):
    visited = [0] * (N+1)
    visited[i] = 1

    queue = deque()
    queue.append(i)
    n = 1
    while queue:
        v = queue.popleft()

        for w in g[v]:
            if visited[w] == 0:
                queue.append(w)
                visited[w] = 1
                n += 1
        
        if max_n < n:
            max_n = n
            ans = {i}
        elif max_n == n:
            ans.add(i)

print(*sorted(ans))