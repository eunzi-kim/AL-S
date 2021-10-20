import sys
input = sys.stdin.readline

n = input().rstrip()

def toTwo(x):
    if x < 2:
        return x
    else:
        return 10*toTwo(x//2) + x%2

ans = ""
for i in range(len(n)):
    x = str(toTwo(int(n[i])))
    if len(x) == 3:
        ans += x
    elif len(x) == 2:
        ans += "0" + x
    else:
        ans += "00" + x

ans = ans.lstrip("0")
if len(ans):
    print(ans)
else:
    print("0")