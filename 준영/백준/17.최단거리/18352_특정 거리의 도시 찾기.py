import sys
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

arr = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())

    arr[x].append(y)

minimum = [int(1e9)] * (N+1)
minimum[X] = 0

q = [(X, 0)]

while q:
    x, t = q.pop(0)
    if t < K:
        for i in arr[x]:
            
            if minimum[i] > t+1:
                minimum[i] = t+1
                q.append((i, t+1))

not_found = True
for i in range(N+1):
    if minimum[i] == K:
        print(i)
        not_found = False

if not_found:
    print(-1)

