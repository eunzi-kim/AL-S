def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        sub_arr = []
        for k in range(len(arr2[0])):
            sub_v = 0
            for j in range(len(arr1[0])):
                sub_v += arr1[i][j] * arr2[j][k]
            sub_arr.append(sub_v)
        answer.append(sub_arr)
    return answer