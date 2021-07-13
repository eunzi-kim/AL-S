def solution(board):
    answer = 0
    n = len(board) # 행 개수
    m = len(board[0]) # 열 개수

    if n == 1 and m == 1 and board[0][0] == 1:
        return 1

    for i in range(1, n):
        for j in range(1, m):
            if board[i][j]:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1])+1
                if answer < board[i][j]:
                    answer = board[i][j]
    # print(board) 
    return answer ** 2

b = [[1]]
print(solution(b))