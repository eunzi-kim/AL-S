import itertools

N, M = map(int, input().split())
arr = list(map(int, input().split()))
result = 0

for i in itertools.combinations(arr, 3):
    if sum(i) <= M and result < sum(i):
        result = sum(i)

print(result)