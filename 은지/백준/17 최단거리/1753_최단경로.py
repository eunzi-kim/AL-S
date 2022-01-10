import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import heapq

V, E = map(int, input().split())
K = int(input())

g =  [[] for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    g[u].append((v, w))

INF = int(1e9)
weight = [INF]*(V+1)

# 시간초과 해결 
# => heapq를 이용하여 가중치가 작은 순서대로 살펴보기!
queue = []
heapq.heappush(queue, (0, K))
weight[K] = 0

while queue:
    val = heapq.heappop(queue)
    c = val[0]
    x = val[1]

    # 가지치기를 통해 시간초과 줄여주기
    if weight[x] < c:
        continue

    for node in g[x]:
        temp = c + node[1]
        i = node[0]
        if temp < weight[i]:
            weight[i] = temp
            heapq.heappush(queue, (temp, i))

for idx in range(1, V+1):
    if weight[idx] == INF:
        print("INF")
    else:
        print(weight[idx])
