N, K = map(int, input().split())

time = 0
result = 0

while True:
    si = time // 3600
    if si == N+1:
        break
    bun = (time % 3600) // 60
    cho = time % 60

    temp = str(si).zfill(2) + str(bun).zfill(2) + str(cho).zfill(2)
    if str(K) in temp:
        result += 1

    time += 1


print(result)