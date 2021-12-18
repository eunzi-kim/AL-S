import sys
input = sys.stdin.readline

N = int(input())
Matrix = [list(map(int, input().split())) for _ in range(N)]

arr = []

for i in range(N):
    for j in range(i+1, N):
        arr.append([Matrix[i][j], i, j])

arr.sort()

zzang = [x for x in range(N)]

def find(x):
    if x != zzang[x]:
        zzang[x] = find(zzang[x])
        return zzang[x]
    else:
        return x

def union(a, b):
    A = find(a)
    B = find(b)

    if A < B:
        zzang[B] = zzang[A]
    elif A > B:
        zzang[A] = zzang[B]

ans = 0

for x in arr:
    v = x[0]
    i = x[1]
    j = x[2]

    if find(i) != find(j):
        union(i, j)
        ans += v

print(ans)