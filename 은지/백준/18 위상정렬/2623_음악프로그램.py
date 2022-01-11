import sys
input = sys.stdin.readline

N, M = map(int, input().split())

indegree = [0]*(N+1)
next = [[] for _ in range(N+1)]

for _ in range(M):
    arr = list(map(int, input().split()))
    for i in range(2, arr[0]+1):
        indegree[arr[i]] += 1
        next[arr[i-1]].append(arr[i])

queue = []
for j in range(1, N+1):
    if indegree[j] == 0:
        queue.append(j)

answer = []
while queue:
    v = queue.pop(0)
    answer.append(v)
    for w in next[v]:
        indegree[w] -= 1
        if indegree[w] == 0:
            queue.append(w)

if len(answer) == N:
    for x in answer:
        print(x)
else:
    print(0)