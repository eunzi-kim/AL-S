left = 13
right = 17

ans = 0
for a in range(left, right+1):
    cnt = 0
    for b in range(1, a+1):
        if a % b == 0:
            cnt +=1

    if cnt % 2 == 0:
        ans += a

    else:
        ans -= a

print(ans)


