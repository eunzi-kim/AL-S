import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())

arr = [[] for _ in range(V+1)]

for _ in range(E):
    A, B, C = map(int, input().split())

    arr[A].append([C, B])
    arr[B].append([C, A])

visit = [False for _ in range(V+1)]
visit[1] = True

queue = []
for i in arr[1]:
    heapq.heappush(queue, i)

while queue:
    dist, node = heapq.heappop(queue)

    if not visit[node]:
        visit[node] = dist
        
        for i in arr[node]:
            heapq.heappush(queue, i)

result = 0
for i in range(2, V+1):
    result += visit[i]

print(result)