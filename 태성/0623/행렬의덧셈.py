def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        pre = []
        for j in range(len(arr1[i])):
            pre.append(arr1[i][j] + arr2[i][j])

        answer.append(pre)
    return answer