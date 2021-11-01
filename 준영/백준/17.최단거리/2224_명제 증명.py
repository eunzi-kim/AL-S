N = int(input())

arr = [[] for _ in range(58)]

for _ in range(N):
    x, temp, y = input().split()

    if x == y: continue

    arr[ord(x)-65].append(ord(y)-65)

result = [[0 for _ in range(58)] for _ in range(58)]
cnt = 0

for i in range(58):
    while arr[i]:
        x = arr[i].pop(0)
        if i == x: continue
        result[i][x] = 1
        for j in arr[x]:
            arr[i].append(j)

for i in range(58):
    for j in range(58):
        if result[i][j]:
            print(f'{chr(i+65)} => {chr(j+65)}')