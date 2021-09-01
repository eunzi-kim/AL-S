def solution(arr1, arr2):
    N = len(arr1)
    M = len(arr1[0])
    N1 = len(arr2)
    M1 = len(arr2[0])
    answer = [[0 for _ in range(M1)] for _ in range(N)]

    for i in range(N):
        for j in range(M1):
            temp = 0
            for k in range(M):
                temp += arr1[i][k] * arr2[k][j]
            answer[i][j] = temp


    return answer

arr1 = [[1, 4], [3, 2], [4, 1]]	
arr2 = [[3, 3], [3, 3]]
solution(arr1, arr2)