def solution(board):
    answer = 0
    N = len(board)
    M = len(board[0])

    max_val = 1
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                my_queue = []
                my_queue.append([i, j])

                temp = 1

                while my_queue:
                    x, y = my_queue.pop(0)

                    if x+1 >= N or y+1 >= M:
                        break

                    is_square = True

                    for k in range(x+1-temp, x+2):
                        if board[k][y] == 0:
                            is_square = False
                            break
                    
                    for l in range(y+1-temp, y+2):
                        if board[x][l] == 0:
                            is_square = False
                            break
                    
                    if is_square:
                        my_queue.append([x+1, y+1])
                        temp += 1

                max_val = max(max_val, temp)

    answer = max_val ** 2

    return answer

board = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]

print(solution(board))