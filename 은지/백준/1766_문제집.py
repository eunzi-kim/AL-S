import sys
input = sys.stdin.readline

N, M = map(int, input().split())

degree = [0] * (N+1)
after = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    degree[B] += 1
    after[A].append(B)

queue = []
for i in range(1, N+1):
    if degree[i] == 0:
        queue.append(i)

answer = []
while queue:
    queue.sort()
    v = queue.pop(0)
    answer.append(v)

    for x in after[v]:
        degree[x] -= 1
        if degree[x] == 0:
            queue.append(x)

print(*answer)