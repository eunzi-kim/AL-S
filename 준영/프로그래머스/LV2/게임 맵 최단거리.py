def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[0 for _ in range(m)] for _ in range(n)]
    my_queue = []
    my_queue.append((0, 0, 1))
    visited[0][0] = 1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while my_queue:
        x, y, d = my_queue.pop(0)

        for i in range(4):
            vx = x + dx[i]
            vy = y + dy[i]

            if vx < 0 or vy < 0 or vx >= n or vy >= m:
                continue
            
            if visited[vx][vy]:
                continue
            
            if maps[vx][vy] == 0:
                continue

            visited[vx][vy] = (d+1)
            
            my_queue.append((vx, vy, d+1))

    answer = visited[n-1][m-1]
    if answer == 0:
        answer = -1
    return answer

maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))