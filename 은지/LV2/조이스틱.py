def solution(name):
    answer = 0
    alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    n = len(name)
    
    for i in range(n):
        j = alpha.index(name[i])
        answer += min(j, 26-j)

    min_m = n-1
    next = 0
    for i in range(n):
        next = i + 1
        while next < n and name[next] == "A":
            next += 1
        
        min_m = min(min_m, 2*i+n-next, i+2*(n-next))
    answer += min_m
    return answer