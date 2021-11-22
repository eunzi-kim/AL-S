N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]


def pulling(n):
    global board

    b = []
    for r in range(0, n, 2):
        temp = []
        for c in range(0, n, 2):
            arr = [board[r][c], board[r+1][c], board[r][c+1], board[r+1][c+1]]
            arr.sort()
            temp.append(arr[2])
        b.append(temp)
        temp = []
    board = b
    return n//2


while len(board[0]) > 1:
    N = pulling(N)

print(board[0][0])