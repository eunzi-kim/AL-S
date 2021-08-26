def solution(m, n, board):
    answer = 0

    arr = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            arr[i][j] = board[j][0]
            board[j] = board[j][1:]

    temp_board = [0 for _ in range(n)]

    while True:
        temp = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n-1):
            for j in range(m-1):
                if arr[i][j] != '' and arr[i][j] == arr[i][j+1] and arr[i][j] == arr[i+1][j] and arr[i][j] == arr[i+1][j+1]:
                    temp[i][j] += 1
                    temp[i+1][j] += 1
                    temp[i][j+1] += 1
                    temp[i+1][j+1] += 1

        isBreak = True

        for i in range(n):
            for j in range(m):
                if temp[i][j] != 0:
                    arr[i][j] = ''
                    isBreak = False
        
        if isBreak: break
        
        for i in range(n):
            temp_board[i] = "".join(arr[i])
        
        for i in range(n):
            for j in range(m):
                if j < m - len(temp_board[i]):
                    arr[i][j] = ''
                else:
                    arr[i][j] = temp_board[i][0]
                    temp_board[i] = temp_board[i][1:]
        
    for i in range(n):
        for j in range(m):
            if arr[i][j] == '':
                answer += 1

    return answer

m = 4
n = 5
board = ["CCBDE",
         "AAADE",
         "AAABF",
         "CCBBF"]
solution(m,n,board)
m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
solution(m,n,board)