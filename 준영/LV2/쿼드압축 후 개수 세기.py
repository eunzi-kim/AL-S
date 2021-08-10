def quard(arr, idx, temp, x, y):
    result = True
    zero_one = arr[x][y]
    for i in range(x, x+idx):
        for j in range(y, y+idx):
            if arr[i][j] != zero_one:
                result = False
    
    if result:
        for i in range(x, x+idx):
            for j in range(y, y+idx):
                temp[i][j] = 1

        return zero_one
    else:
        return -1

def solution(arr):
    n = len(arr)
    temp = [[0 for _ in range(n)] for _ in range(n)]
    answer = [0, 0]

    idx = n
    while idx >= 1:
        for i in range(0, n, idx):
            for j in range(0, n, idx):
                if temp[i][j] == 0:
                    zo = quard(arr, idx, temp, i, j)
                    if zo != -1:
                        answer[zo] += 1

        idx //= 2

    return answer


arr = [[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]	
solution(arr)