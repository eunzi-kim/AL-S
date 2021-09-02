n = int(input())
m = int(input())
com = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    com[s].append(e)
    com[e].append(s)
cnt = 0
queue = [1]
chk = [0] * (n+1)
chk[1] = 1
while queue:
    v = queue.pop(0)
    for w in com[v]:
        if chk[w] == 0:
            queue.append(w)
            chk[w] = 1
            cnt += 1
print(cnt)