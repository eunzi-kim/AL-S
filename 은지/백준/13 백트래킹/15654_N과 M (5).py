from itertools import permutations

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

for v in permutations(arr, M):
    print(*v)