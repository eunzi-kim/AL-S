N, M = map(int, input().split())

rank = [[i, 0] for i in range(N+1)]
indegree = [0] * (N+1)
child = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    child[A].append(B)
    indegree[B] += 1

queue = []

for i in range(1, N+1):
    if indegree[i] == 0:
        rank[i][1] = 1
        queue.append(i)

while queue:
    v = queue.pop(0)
    for w in child[v]:
        if indegree[w] == 1:
            rank[w][1] = rank[v][1]+1
            queue.append(w)
        indegree[w] -= 1

rank.sort(key=lambda x: x[1])

result = ''
for i in range(1, N+1):
    result += str(rank[i][0])
    result += ' '
result.rstrip()
print(result)
