import sys
input = sys.stdin.readline
 
N, M = map(int, input().split())

parent = [i for i in range(N+1)]

def find(target):
    if target == parent[target]:
        return target
    else:
        parent[target] = find(parent[target])
        return parent[target]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

roads = []

for i in range(M):
    A, B, C = map(int, input().split())
    roads.append((C, A, B))

roads.sort()

result = []

for c, a, b in roads:
    if find(a) != find(b):
        union(a, b)
        result.append(c)

print(sum(result)-max(result))
