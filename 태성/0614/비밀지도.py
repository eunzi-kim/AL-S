n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]


def mk_2(k, n):
    res = []
    while k>0:
        j = k%2
        res.append(j)
        k = k//2

    d = n - len(res)

    l_res = list(reversed(res))


    pre_res = [0]*d
    res = pre_res + l_res

    return res


# print(mk_2(5, 5))

def solution(n, arr1, arr2):
    answer = []

    board1 = []
    for a1 in arr1:
        board1.append(mk_2(a1, n))

    print(board1)

    board2 = []
    for a2 in arr2:
        board2.append(mk_2(a2, n))

    print(board2)

    for i in range(n):
        pre = ""
        for j in range(n):
            if board1[i][j] == 1 or board2[i][j] == 1:
                pre += "#"
            else:
                pre += " "

        answer.append(pre)

    return answer


print(solution(n, arr1, arr2))