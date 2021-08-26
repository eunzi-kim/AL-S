def solution(n):
    answer = 0

    result = []
    temp = n
    while temp:
        result.append(temp%2)
        temp //= 2

    idx = 0
    while True:
        idx += 1
        arr = []
        temp = n + idx
        while temp:
            arr.append(temp%2)
            temp //= 2

        if arr.count(1) == result.count(1):
            answer = n + idx
            break

    return answer