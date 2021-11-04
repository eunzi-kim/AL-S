import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [[] for _ in range(N+1)]

for i in range(M):
    A, B, C = map(int, input().split())
    heapq.heappush(arr[A], [C, B])
    heapq.heappush(arr[B], [C, A])
    
visit = [False for i in range(N+1)]
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

sum_result = 0
for i in range(2, N+1):
    sum_result += visit[i]

print(sum_result-max(visit[2:]))