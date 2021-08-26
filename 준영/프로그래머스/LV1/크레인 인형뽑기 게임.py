def solution(board, moves):
    answer = 0
    length = len(board)
    depth = [0]*length

    for i in range(length):
        for j in range(length):
            if board[j][i]:
                depth[i] = length - j
                break

    stack = []

    for i in moves:
        if depth[i-1]:
            if len(stack) > 0 and stack[-1] == board[length-depth[i-1]][i-1]:
                stack.pop()
                answer += 2
            else:
                stack.append(board[length-depth[i-1]][i-1])
            depth[i-1] -= 1
    

    return answer

x = solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])
print(x)