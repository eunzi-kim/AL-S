def solution(maps):
    n = len(maps)
    m = len(maps[0])
    check = [[0]*m for _ in range(n)]
    queue = [(0, 0)]
    check[0][0] = 1
    # 상 하 좌 우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    while queue:
        v = queue.pop(0)
        r = v[0]
        c = v[1]
        for i in range(4):
            new_r = r + dr[i]
            new_c = c + dc[i]
            if 0 <= new_r < n and 0 <= new_c < m and maps[new_r][new_c] and check[new_r][new_c] == 0:
                queue.append((new_r, new_c))
                check[new_r][new_c] = check[r][c] + 1
    if check[n-1][m-1]:
        answer = check[n-1][m-1]
    else:
        answer = -1
    return answer

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]	
print(solution(maps))