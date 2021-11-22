N = int(input())

result = 0
for i in range(1, N):
    x = str(i)
    temp = 0
    for j in x:
        temp += int(j)
    if i + temp == N:
        result = i
        break

print(result)