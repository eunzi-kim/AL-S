def solution(land):
    answer = 0

    N = len(land)
    M = len(land[0])

    d_arr = [[0 for _ in range(M)] for _ in range(N)]
    
    for i in range(M):
        d_arr[0][i] = land[0][i]

    for i in range(1, N):
        for j in range(M):
            max_temp = 0
            for k in range(M):
                if j == k: continue

                if max_temp < d_arr[i-1][k]:
                   max_temp = d_arr[i-1][k]
            d_arr[i][j] = land[i][j] + max_temp
    answer = max(d_arr[i])
    return answer

# land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
# solution(land)
land = [[1,1,1,1],[2,2,2,3],[3,3,3,6],[4,4,4,7]]
solution(land)