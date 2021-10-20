import sys
input = sys.stdin.readline

N, M = map(int, input().split())

g = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    g[B].append(A)

max_n = 0
ans = set()
for i in range(1, N+1):
    visited = [0] * (N+1)
    visited[i] = 1

    stack = [[i, 0]]
    while stack:
        x = stack.pop(0)
        v = x[0]
        n = x[1]

        if max_n < n:
            max_n = n
            ans = {i}
        elif max_n == n:
            ans.add(i)

        for w in g[v]:
            if visited[w] == 0:
                visited[w] = 1
                stack.append([w, n+1])

print(*sorted(ans))

# result = ""
# for x in ans:
#     result += str(x) + " "

# print(result)