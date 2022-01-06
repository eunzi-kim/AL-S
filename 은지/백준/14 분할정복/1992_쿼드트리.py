N = int(input())
board = [list(input()) for _ in range(N)]

ans = ""


def chk(r, c, n):
    temp = board[r][c]

    for i in range(n):
        for j in range(n):
            if temp != board[r+i][c+j]:
                return 0
    return temp


def search(r, c, n):
    global ans

    v = chk(r, c, n)
    if v == 0:
        # 한 세트씩 괄호 넣어주기!
        ans += "("
        search(r, c, n//2)
        search(r, c+n//2, n//2)
        search(r+n//2, c, n//2)        
        search(r+n//2, c+n//2, n//2)
        ans += ")"
    else:
        ans += v


search(0, 0, N)

print(ans)