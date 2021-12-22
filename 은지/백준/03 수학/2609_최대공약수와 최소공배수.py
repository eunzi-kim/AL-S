N, M = map(int, input().split())
p = min(N, M)
gcd = 0
for x in range(p, 0, -1):
    if N % x == 0 and M % x == 0:
        gcd = x
        break

print(gcd)
print(N*M//gcd)