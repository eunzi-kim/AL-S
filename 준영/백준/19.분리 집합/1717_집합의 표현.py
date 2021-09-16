import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

N, M = map(int, input().split())

parent = [x for x in range(N+1)]

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

for _ in range(M):
    x, a, b = map(int, input().split())

    if x == 0:
        union(a, b)

    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')


