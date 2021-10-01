import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

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

arr = []

for i in range(1, N+1):
    city = list(map(int, input().split()))
    for j in range(1, N+1):
        if city[j-1] == 1:
            union(i, j)

result = True

tour = list(map(int, input().split()))
temp = parent[tour[0]]
for i in tour:
    if temp != parent[i]:
        result = False

if result:
    print('YES')
else:
    print('NO')
