N, M = map(int, input().split())

ans = []

def search(i):
    if i == M:
        print(*ans)
        return

    for j in range(1, N+1):
        ans.append(str(j))
        search(i+1)
        ans.pop(-1)

search(0)