def solution(m, n, board):
    b = []
    for r in range(m):
        sub_b = []
        for c in range(n):
            sub_b.append(board[r][c])
        b.append(sub_b)
    
    dr = [0, 1, 0, 1]
    dc = [0, 0, 1, 1]
    answer = 0
    while True:
        chk = [[0]*n for _ in range(m)]
        cnt = 0
        for r in range(m-1):
            for c in range(n-1):
                friends = b[r][c]
                if friends != "0":                    
                    for i in range(1, 4):
                        if b[r+dr[i]][c+dc[i]] != friends:
                            break
                    else:
                        cnt += 1
                        for j in range(4):
                            chk[r+dr[j]][c+dc[j]] = 1

        if cnt == 0:
            break

        for r in range(m):
            for c in range(n):
                if chk[r][c] == 1:
                    answer += 1
                    for k in range(r-1, -1, -1):
                        b[k+1][c] = b[k][c]
                    b[0][c] = "0"
    return answer

m = 5
n = 6
b = ["AAAAAA", "BBAATB", "BBAATB", "JJJTAA", "JJJTAA"]
print(solution(m, n, b))

# print(solution(2, 4, ["baab", "baab"]))