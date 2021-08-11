zero = one = 0

def search(r, c, n, arr):
    global zero, one

    chk = 1
    for i in range(r, r+n):
        for j in range(c, c+n):
            if arr[r][c] != arr[i][j]:
                chk = 0
                break
        if chk == 0:
            break
    if chk == 1:
        if arr[r][c] == 1:
            one += 1
        else:
            zero += 1
    else:
        for k in range(r, r+n, n//2):
            for l in range(c, c+n, n//2):
                search(k, l, n//2, arr)


def solution(arr):
    search(0, 0, len(arr), arr)
    answer = [zero, one]
    return answer