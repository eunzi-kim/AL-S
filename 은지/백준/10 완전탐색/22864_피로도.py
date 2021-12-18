A, B, C, M = map(int, input().split())

work = 0
p = 0
for _ in range(24):
    if p + A <= M:
        work += B
        p += A
    else:
        if p-C < 0:
            p = 0
        else:
            p -= C
print(work)