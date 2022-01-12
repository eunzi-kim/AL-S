import sys
input = sys.stdin.readline

N = int(input())

zzang = [x for x in range(1000001)]
cnt = [1]*1000001


def find(x):
    if zzang[x] != x:
        zzang[x] = find(zzang[x])
        return zzang[x]
    else:
        return x

def union(a, b):
    A = find(a)
    B = find(b)

    if A < B:
        zzang[B] = zzang[A]
        cnt[A] += cnt[B]
        cnt[B] = 0
    elif A > B:
        zzang[A] = zzang[B]
        cnt[B] += cnt[A]
        cnt[A] = 0
    

for _ in range(N):
    arr = list(input().split())
    if arr[0] == "I":
        union(int(arr[1]), int(arr[2]))
    elif arr[0] == "Q":
        print(cnt[find(int(arr[1]))])