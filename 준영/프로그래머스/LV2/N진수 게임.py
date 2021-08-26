def solution(n, t, m, p):
    answer = ''
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    result = [0]

    for i in range(1, m*t+1):
        temp = []
        while i:
            temp.insert(0, arr[i % n]) 
            i //= n
        
        for i in temp:
            result.append(i)
            if len(result) >= m*t:
                break
        if len(result) >= m*t:
            break
    
    for i in range(p-1, len(result), m):
        answer += str(result[i])
    
    return answer


n = 2
t = 4
m = 2
p = 1
solution(n, t, m, p)
n = 16
t = 16
m = 2
p = 1
solution(n, t, m, p)