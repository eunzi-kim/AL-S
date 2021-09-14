import sys
input = sys.stdin.readline

N, R, Q = map(int, input().split())

arr = [[] for _ in range(N+1)]
visit = [True for _ in range(N+1)]
result = [0 for _ in range(N+1)]

for _ in range(1, N):
    U, V = map(int, input().split())
    arr[U].append(V)
    arr[V].append(U)

q = []

for i in range(N+1):
    if len(arr[i]) == 1 and i != R:
        q.append([i, 0])

while q:
    x, dist = q.pop(0)

    if visit[x]:
        result[x] = 1
        result[x] += dist
        dist += 1
    else:
        result[x] += dist

    visit[x] = False

    if x == R:
        continue

    for i in arr[x]:
        if visit[i]:
            q.append([i, result[x]])
    

for _ in range(Q):
    U = int(input())
    print(result[U])
    
