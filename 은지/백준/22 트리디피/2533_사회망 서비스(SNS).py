import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline 

N = int(input())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

ans = set()
visited = [0]*(N+1)

def dfs(x):
    visited[x] = 1

    if len(tree[x]) <= 1:  # 단말노드
        return True

    else:
        for y in tree[x]:
            if visited[y] == 0:
                # 친구가 단말노드 or 얼리어답터가 아님
                if dfs(y):
                    ans.add(x)
                elif y not in ans:
                    ans.add(x)

        # 단말노드 X
        return False

for i in range(1, N+1):
    if len(tree[i]) > 1:
        dfs(i)
        break

if N == 2:
    print(1)
else:
    print(len(ans))