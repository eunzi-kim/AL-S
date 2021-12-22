import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

tree = [[] for _ in range(N)]
queue = []

for i in range(N):
    if arr[i] != -1:
        tree[arr[i]].append(i)
    else:
        queue.append(i)

n = int(input())

cnt = 0
while queue:
    v = queue.pop(0)

    if v == n:
        continue

    if len(tree[v]) == 0 or tree[v] == [n]:
        cnt += 1

    for w in tree[v]:
        if w != n:
            queue.append(w)

print(cnt)