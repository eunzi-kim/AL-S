def solution(land):
    for i in range(len(land)-1):
        land[i+1][0] += max(land[i][1], land[i][2], land[i][3])
        land[i+1][1] += max(land[i][0], land[i][2], land[i][3])
        land[i+1][2] += max(land[i][1], land[i][0], land[i][3])
        land[i+1][3] += max(land[i][1], land[i][2], land[i][0])
    n = len(land)
    answer = max(land[n-1])
    return answer

land = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(land))