N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

ans = []


def pick(idx):
    if len(ans) == M:
        print(*ans)
        return

    for i in range(idx, N):
        ans.append(arr[i])
        pick(i+1)
        ans.pop(-1)


pick(0)