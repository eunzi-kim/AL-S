import sys
input = sys.stdin.readline

parent = [x for x in range(1000001)]
parent_cnt = [1 for x in range(1000001)]

def find(target):
    if target == parent[target]:
        return target
    else:
        parent[target] = find(parent[target])
        return parent[target]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        if a < b:
            parent[b] = a
            parent_cnt[a] += parent_cnt[b]
        else:
            parent[a] = b
            parent_cnt[b] += parent_cnt[a]

N = int(input())
result = []
for _ in range(N):
    temp = list(input().split())

    if temp[0] == 'I':
        union(int(temp[1]), int(temp[2]))
    else:
        x = find(int(temp[1]))
        result.append(parent_cnt[x])

print("\n".join(map(str, result)))