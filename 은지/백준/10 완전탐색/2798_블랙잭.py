import itertools

N, M = map(int, input().split())
arr = list(map(int, input().split()))

v = itertools.combinations(arr, 3)

ans = 0
for w in v:
    s_v = sum(w)
    if ans < s_v <= M :
        ans = s_v

print(ans)