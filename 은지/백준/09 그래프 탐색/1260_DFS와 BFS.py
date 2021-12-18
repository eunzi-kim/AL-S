N, M, V = map(int, input().split())
g = [[] for _ in range(N+1)]
for _ in range(M):
    s, e = map(int, input().split())
    g[s].append(e)
    g[s].sort()
    g[e].append(s)
    g[e].sort()
    

# DFS
d_ans = []
stack = [V]
while stack:
    v = stack.pop(-1)
    if v not in d_ans:
        d_ans.append(v)
        for i in range(len(g[v])-1, -1, -1):
            if g[v][i] not in d_ans:
                stack.append(g[v][i])

print(*d_ans)


# BFS
b_ans = []
queue = [V]
while queue:
    v = queue.pop(0)
    if v not in b_ans:
        b_ans.append(v)
        for w in g[v]:
            if w not in b_ans:
                queue.append(w)

print(*b_ans)