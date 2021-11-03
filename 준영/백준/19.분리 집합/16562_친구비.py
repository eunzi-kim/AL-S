N, M, K = map(int, input().split())

arr = list(map(int, input().split()))
arr = [0] + arr
parent = [x for x in range(N+1)]

def find(target):
    if target == parent[target]:
        return target
    else:
        parent[target] = find(parent[target])
        return parent[target]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(M):
    v, w = map(int, input().split())
    union(v, w)

for i in range(1, N+1):
    if parent[parent[i]] != parent[i]:
        parent[i] = parent[parent[i]]

result = {}

for i in range(1, N+1):
    if result.get(parent[i]):
        if result.get(parent[i]) > arr[i]:
            result[parent[i]] = arr[i]
    else:
        result[parent[i]] = arr[i]

sum_result = 0
for key, value in result.items():
    sum_result += value

if sum_result <= K:
    print(sum_result)
else:
    print("Oh no")
