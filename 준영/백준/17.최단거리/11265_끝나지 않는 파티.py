import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [[0] * (N+1)]

for i in range(N):
    arr.append([0] + list(map(int, input().split())))

temp = [[9999999999 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    visit = [False for _ in range(N+1)]
    q = []

    heapq.heappush(q, [0, i])

    while q:
        dist, now = heapq.heappop(q)
        
        if visit[now]:
            continue

        for j in range(1, N+1):
            if arr[now][j] + dist < temp[i][j]:
                temp[i][j] = arr[now][j] + dist
                heapq.heappush(q, [arr[now][j] + dist, j])
            
        visit[now] = True

for i in range(M):
    A, B, C = map(int, input().split())

    if temp[A][B] <= C:
        print('Enjoy other party')
    else:
        print('Stay here')