def solution(arr):
    n = len(arr)
    chk = []
    zero = one = 0
    while n > 0:
        for r in range(0, len(arr), n):
            for c in range(0, len(arr), n):
                if [r, c] not in chk:
                    i = j = 0
                    while i <= n and j <= n:
                        if arr[r+i][c+j] == arr[r][c]:
                            if i == n-1 and j == n-1:
                                for k in range(r, r+n):
                                    for l in range(c, c+n):
                                        chk.append([k, l])
                                if arr[r][c] == 1:
                                    one += 1
                                else:
                                    zero += 1
                                break
                            if i < n-1:
                                i += 1
                            else:
                                i = 0
                                j += 1
                        else:
                            break
        n //= 2
        # print(chk)
    answer = [zero, one]
    return answer

arr = [[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
print(solution(arr))