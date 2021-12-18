import itertools

N, M = map(int, input().split())

arr = [x for x in range(1, N+1)]

v = itertools.combinations(arr, M)

for w in v:
    print(*w)