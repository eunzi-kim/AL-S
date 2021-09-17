import sys
input = sys.stdin.readline

def poly(cnt, ans):
    if cnt // 4:
        ans += "AAAA" * (cnt // 4)
        cnt = cnt % 4
    if cnt // 2:
        ans += "BB" * (cnt // 2)
        cnt = 0
    return ans

s = input()

ans = ""
cnt = 0
for x in s:
    if x == "X":
        cnt += 1
    elif x == ".":
        if cnt % 2:
            ans = -1
            break

        else:
            ans = poly(cnt, ans)
            ans += "."
            cnt = 0

if ans != -1 and cnt % 2 == 0:
    ans = poly(cnt, ans)
    cnt = 0

if cnt:
    ans = -1

print(ans)

############################################

s = input()
s = s.replace("XXXX", "AAAA")
s = s.replace("XX", "BB")

if "X" in s:
    print(-1)
else:
    print(s)