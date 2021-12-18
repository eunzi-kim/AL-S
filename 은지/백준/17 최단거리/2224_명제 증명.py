N = int(input())
g = [[0]*58 for _ in range(58)]

cnt = 0
for _ in range(N):
    arr = list(input().split())
    a = arr[0]
    b = arr[-1]
    if a != b and g[ord(a)-65][ord(b)-65] == 0:
        cnt += 1
        g[ord(a)-65][ord(b)-65] = 1

for i in range(58):
    for j in range(58):
        for k in range(58):
            # if i != k and g[i][j] and g[j][k] and g[i][k] == 0:
            #     g[i][k] = 1
            #     cnt += 1
            if j != k and g[j][i] and g[i][k] and g[j][k] == 0:
                g[j][k] = 1
                cnt += 1
                
print(cnt)
for i in range(58):
    for j in range(58):
        if g[i][j]:
            print(chr(i+65) + " => " + chr(j+65))