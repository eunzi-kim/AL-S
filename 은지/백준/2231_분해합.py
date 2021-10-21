N = int(input())

ans = 0
for x in range(1, N+1):
    temp = x
    v = str(x)
    for i in range(len(v)):
        temp += int(v[i])

    if temp == N:
        ans = x
        break

print(ans)