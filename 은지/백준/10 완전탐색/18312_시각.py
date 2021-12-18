import sys
input = sys.stdin.readline

N, K = map(int, input().split())

ans = 0
hour = minute = second = ""

for h in range(0, N+1):
    if h < 10:
        hour = "0" + str(h)
    else:
        hour = str(h)

    for m in range(0, 60):
        if m < 10:
            minute = "0" + str(m)
        else:
            minute = str(m)

        for s in range(0, 60):
            if s < 10:
                second = "0" + str(s)
            else:
                second = str(s)

            time = hour + minute + second
            if str(K) in time:
                ans += 1

print(ans)