def bfs(r, c, maps):
    visited = [[False]*len(maps[0]) for _ in range(len(maps))]
    stack = []
    
    stack.append((r, c, 1))
    visited[r][c] = True
    while stack:
        r, c, cnt = stack.pop(0)

        for dr, dc in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            n_r = r + dr
            n_c = c + dc
            if 0 <= n_c < len(maps[0]) and 0 <= n_r < len(maps) and not visited[n_r][n_c]:
                if maps[n_r][n_c] == 1:
                    stack.append((n_r, n_c, cnt+1))
                    visited[n_r][n_c] = True
                    if n_c == len(maps[0])-1 and n_r == len(maps)-1:

                        return stack.pop()[2]

    return -1

def solution(maps):
    answer = 0
    answer = bfs(0, 0, maps)
    # print(bfs(0, 0, maps))

    return answer