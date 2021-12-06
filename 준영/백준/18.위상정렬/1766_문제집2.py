import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

indegree = [0] * (N+1)
child = [[] for _ in range(N+1)]

for _ in range(M):
    X, Y = map(int, input().split())
    child[X].append(Y)
    indegree[Y] += 1

queue = []

for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(queue, i)

result = []

while queue:
    x = heapq.heappop(queue)
    
    result.append(x)

    for i in child[x]:
        if indegree[i] == 1:
            heapq.heappush(queue, i)
        indegree[i] -= 1

print(" ".join(map(str, result)))