import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())

zzang = [x for x in range(n+1)]

def search(x):
    if zzang[x] == x:  # 재귀에서 basecase는 위로 올려주기
        return x
    else:
        zzang[x] = search(zzang[x])
        return zzang[x]

def change(a, b):
    A = search(a)
    B = search(b)
    if A < B:
        zzang[B] = A
    else:
        zzang[A] = B

for _ in range(m):
    chk, a, b = map(int, input().split())
    if chk == 0:
        change(a, b)
    else:
        if search(a) == search(b):
            print("YES")
        else:
            print("NO")