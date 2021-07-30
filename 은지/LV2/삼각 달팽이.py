def solution(n):
    answer = []
    lst = [[] for _ in range(n)]
    max_x = 0
    for y in range(1, n+1):
        max_x += y
    x = 1
    c = 0
    d = "-"
    chk = [0]*(n+1)
    while x <= max_x:
        if len(lst[c]) < c+1 and chk[c] == 0:
            lst[c].append([x, d])
            x += 1     
            
        if c+1 < n and chk[c+1] == 0 and d == "+":
            c += 1
        elif chk[c-1] == 0 and d =="-":
            c -= 1
                               
        if len(lst[c]) == c+1:
            chk[c] = 1
            if d == "+":
                d = "-"
            else:
                d = "+"

    for i in range(n):        
        for j in range(0, i+1):
            if lst[i][j][1] == "+":
                answer.append(lst[i][j][0])
        for j in range(i, -1, -1):
            if lst[i][j][1] == "-":
                answer.append(lst[i][j][0])

    return answer

n = 6
print(solution(n))