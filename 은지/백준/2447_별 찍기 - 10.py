import sys
input = sys.stdin.readline

N = int(input())

board = [["*"]*N for _ in range(N)]


def blank(r, c, x):
    if x == 0:
        space = 1
    else:
        space = 3**x
        
    for i in range(r+space, r+(2*space)):
        for j in range(c+space, c+(2*space)):
            board[i][j] = " "    

n = N
yang = 0
while n > 1:
    yang += 1
    n //= 3

for k in range(1, yang+1):
    for new_r in range(0, N, 3**k):
        for new_c in range(0, N, 3**k):
            blank(new_r, new_c, k-1)

for k in range(N):
    print("".join(board[k]))