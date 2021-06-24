def solution(board, moves):
    pre = [0]
    answer = 0
    for j in moves:
        for i in range(len(board)):
            if board[i][j-1] != 0:
                if pre[-1] != board[i][j-1]:
                    pre.append(board[i][j-1])
                    board[i][j-1] = 0
                    break
                else:
                    pre.pop()
                    answer += 2
                    board[i][j-1] = 0
                    break
    return answer