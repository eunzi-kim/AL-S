board = list([0]*15 for _ in range(5))

max_c = 0

for i in range(5):
    arr = list(input())
    if len(arr) > max_c:
        max_c = len(arr)
    for j in range(len(arr)):
        board[i][j] = arr[j]

ans = ""
for c in range(max_c):
    for r in range(5):
        if board[r][c]:
            ans += board[r][c]

print(ans)