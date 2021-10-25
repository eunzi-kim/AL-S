import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, c = map(int, input().split())

    if a != b:
        arr[b].append([c, a])
    arr[a].append([c, b])

visit = [False for _ in range(N+1)]
visit[1] = True

q = []

for i in arr[1]:
    heapq.heappush(q, i)

while q:
    dist, x = heapq.heappop(q)

    if not visit[x]:
        visit[x] = dist

        for i in arr[x]:
            if not visit[i[1]]:
                heapq.heappush(q, i)

result = 0

for i in range(2, N+1):
    result += visit[i]

print(result)