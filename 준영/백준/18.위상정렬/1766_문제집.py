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
visit = [False] * (N+1)

for i in range(1, N+1):
    if indegree[i] == 0:
        queue.append(i)
        visit[i] = True
        break
result = []

while queue:
    x = queue.pop(0)
    
    result.append(x)
    
    visit[x] = True

    for i in child[x]:
        indegree[i] -= 1

    for i in range(1, N+1):
        if indegree[i] == 0 and not visit[i]:
            queue.append(i)
            break
    

print(" ".join(map(str, result)))