N = int(input())

g = {}

for _ in range(N):
    i, l, r = input().split()
    g[i] = [l, r]

# 전위 순회
pre_ans = "A"
def pre(x):
    global pre_ans

    if g[x][0] != '.':
        pre_ans += g[x][0]
        pre(g[x][0])
    
    if g[x][1] != ".":
        pre_ans += g[x][1]
        pre(g[x][1])

pre('A')
print(pre_ans)


# 중위 순회
mid_ans = ""
def mid(x):
    global mid_ans

    if g[x][0] != ".":
        mid(g[x][0])

    mid_ans += x

    if g[x][1] != ".":
        mid(g[x][1])

mid("A")
print(mid_ans)


# 후위 순회
back_ans = ""
def back(x):
    global back_ans

    if g[x][0] != ".":
        back(g[x][0])

    if g[x][1] != ".":
        back(g[x][1])

    back_ans += x

back("A")
print(back_ans)