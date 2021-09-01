def solution(n):
    answer = []

    total = 0
    temp = []
    
    for i in range(1, n+1):
        temp.append([0 for _ in range(i)])
        total += i

    move = n

    now = 0

    i = -1
    j = 0

    direction = 0
    
    while now < total:
        direction %= 3

        if direction == 0:
            for t in range(move):
                i += 1
                now += 1
                temp[i][j] = now
        
        if direction == 1:
            for t in range(move):
                j += 1
                now += 1
                temp[i][j] = now

        if direction == 2:
            for t in range(move):
                i -= 1
                j -= 1
                now += 1
                temp[i][j] = now

        move -= 1
        direction += 1

    for t in temp:
        for i in t:
            answer.append(i)
    return answer

solution(4)