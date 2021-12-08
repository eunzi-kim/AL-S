import heapq
import sys
input = sys.stdin.readline

N = int(input())

arr = []
visit = [False for i in range(N+1)]

for i in range(N):
    arr.append(list(map(int, input().split())))

q = []

heapq.heappush(q, [0, 0])
result = [0 for i in range(N)]

while q:
    dist, now = heapq.heappop(q)
    if visit[now]:
        continue
    visit[now] = True
    result[now] = dist

    for i in range(N):
        if not visit[i]:
            heapq.heappush(q, [arr[now][i], i])

print(sum(result))