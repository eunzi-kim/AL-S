def is_partition(arr, x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    ddx = [-2, 2, 0, 0]
    ddy = [0, 0, 2, -2]

    for i in range(4):
        vx = x + dx[i]
        vy = y + dy[i]

        if vx < 0 or vy < 0 or vx >= 5 or vy >= 5:
            continue

        if arr[vx][vy] == 'P':
            return False

        vvx = x + ddx[i]
        vvy = y + ddy[i]

        if vvx < 0 or vvy < 0 or vvx >= 5 or vvy >= 5:
            continue

        if arr[vvx][vvy] == 'P' and arr[vx][vy] != 'X':
            return False

    dddx = [-1, -1, 1, 1]
    dddy = [-1, 1, -1, 1]

    dz = [[0, 3], [0, 2], [1, 3], [1, 2]]

    for i in range(4):
        vx = x + dddx[i]
        vy = y + dddy[i]

        if vx < 0 or vy < 0 or vx >= 5 or vy >= 5:
            continue

        if arr[vx][vy] == 'P':
            dz1 = dz[i][0]
            dz2 = dz[i][1]

            vvx = x + dx[dz1]
            vvy = y + dy[dz1]

            vvvx = x + dx[dz2]
            vvvy = y + dy[dz2]

            if arr[vvx][vvy] != 'X' or arr[vvvx][vvvy] != 'X':
                return False
    return True

def solution(places):
    answer = []
    
    for place in places:
        temp = []
        for p in place:
            temp.append(list(p))
        
        is_space = True

        for i in range(5):
            if is_space:
                for j in range(5):
                    if temp[i][j] == 'P':
                        if not is_partition(temp, i, j):
                            is_space = False
                            break
        
        if is_space:
            answer.append(1)
        else:
            answer.append(0)
                    

    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
solution(places)