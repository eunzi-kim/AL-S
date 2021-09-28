n = int(input())

ans = int(n**(1/2))

while ans**2 < n:
    ans += 1

print(ans)