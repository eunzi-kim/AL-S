N = int(input())
M = int(input())
arr = []
for _ in range(M):
    a, b, c = map(int, input().split())
    arr.append([c, a-1, b-1])

arr.sort()
root = [y for y in range(N)]


def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]


ans = 0

for v in arr:
    a = v[1]
    b = v[2]
    parent_a = find(a)
    parent_b = find(b)
    if parent_a != parent_b:
        min_v = min(root[parent_a], root[parent_b])
        root[parent_a] = min_v
        root[parent_b] = min_v
        find(a)
        find(b)
        ans += v[0]

print(ans)