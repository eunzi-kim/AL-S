from itertools import permutations

N, M = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

for i in permutations(arr, M):
    print(*i)