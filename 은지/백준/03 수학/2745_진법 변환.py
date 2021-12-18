N, B = input().split()

B = int(B)

ans = 0
for i in range(len(N)-1, -1, -1):
    # A ~ Z
    if 65 <= ord(N[i]) <= 90:
        ans += (ord(N[i])-55) * (B ** (len(N)-i-1))
    # 0 ~ 9
    else:
        ans += int(N[i]) * (B ** (len(N)-i-1))
        
print(ans)