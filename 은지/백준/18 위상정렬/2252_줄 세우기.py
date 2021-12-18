import sys
input = sys.stdin.readline

N, M = map(int, input().split())

inDegree = [0] * (N+1)
tall = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    tall[A].append(B)
    inDegree[B] += 1

queue = []
for i in range(1, N+1):
    if inDegree[i] == 0:
        queue.append(i)

ans = []
while queue:
    v = queue.pop(0)
    ans.append(v)
    for w in tall[v]:
        inDegree[w] -= 1
        if inDegree[w] == 0:
            queue.append(w)

print(*ans)