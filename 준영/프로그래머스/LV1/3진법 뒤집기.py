def solution(n):
    answer = 0
    arr = [0] * 19

    idx = 0
    while n:
        arr[idx] = n // (3 ** (18-idx))
        n %= (3 ** (18-idx))
        idx += 1
        
    for i in range(19):
        if arr[i] != 0:
            new_arr = arr[i:]
            break

    for i in range(len(new_arr)):
        answer += ((3 ** i) * new_arr[i])

    
    return answer

print(solution(45))
