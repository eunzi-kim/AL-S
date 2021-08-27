import sys
input = sys.stdin.readline

N = int(input())

tree = [[] for _ in range(N+1)]

uptree = [0 for _ in range(N+1)]

for i in range(N-1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)

q = [1]

while q:
    idx = q.pop(0)

    for i in tree[idx]:
        if uptree[i] == 0:
            uptree[i] = idx
            q.append(i)
        
for i in range(2, N+1):
    print(uptree[i])