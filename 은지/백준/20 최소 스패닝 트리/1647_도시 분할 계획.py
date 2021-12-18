import sys
input = sys.stdin.readline

N, M = map(int, input().split())

info = []
for _ in range(M):
    A, B, C = map(int, input().split())
    info.append([C, A, B])

info.sort()

parent = [x for x in range(N+1)]

def find(x):
    if x == parent[x]:
        return x
    parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    parent_a = find(a)
    parent_b = find(b)
    if parent_a <= parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b

ans = val = 0
for i in range(M):
    [C, A, B] = info[i]
    if find(A) != find(B):
        union(A, B)
        ans += C
        val = C

print(ans-val)