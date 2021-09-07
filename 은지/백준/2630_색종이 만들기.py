n = int(input())
paper = [list(map(int, input().split())) for _ in range(n)]

ans_b = ans_w = 0

queue = [[0, 0, n]]
while queue:
    v = queue.pop(0)
    r = v[0]
    c = v[1]
    m = v[2]

    chk = chk_p = paper[r][c]
    for i in range(r, r+m):
        for j in range(c, c+m):
            if paper[i][j] != chk:
                chk_p = paper[i][j]
                break
        if chk != chk_p:
            break

    if chk == chk_p == 1:
        ans_b += 1
    elif chk == chk_p == 0:
        ans_w += 1
    else:
        w = m // 2
        queue.append([r, c, w])
        queue.append([r, c+w, w])
        queue.append([r+w, c, w])
        queue.append([r+w, c+w, w])

print(ans_w)
print(ans_b)