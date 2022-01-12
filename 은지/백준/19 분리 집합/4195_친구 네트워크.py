import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    F = int(input())

    info = {}
    cnt = {}

    def find(x):
        if x != info[x]:
            cnt[info[x]] += cnt[x]
            cnt[x] = 0
            info[x] = find(info[x])
        return info[x]

    def union(a, b):
        aa = find(a)
        bb = find(b)

        if aa != bb:
            info[aa] = info[bb]
        return aa

    for _ in range(F):
        A, B = input().split()

        if A not in info:
            info[A] = A
            cnt[A] = 1

        if B not in info:
            info[B] = B
            cnt[B] = 1

        i = union(A, B)

        print(cnt[find(i)])