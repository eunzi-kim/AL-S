def solution(dirs):
    answer = 0
    record = []
    now = (0, 0)
    for dir in dirs:
        r = now[0]
        c = now[1]
        if dir == "U":
            r = now[0] + 1
        elif dir == "D":
            r = now[0] - 1
        elif dir == "R":
            c = now[1] + 1
        else:
            c = now[1] - 1
            
        if -5 <= r <= 5 and -5 <= c <= 5:
            record.append(sorted(([now[0], now[1]], [r, c])))
            now = (r, c)
    
    record.sort()
    past = []
    for v in record:
        if past != v:
            answer += 1
            past = v
        
    return answer

dirs = "LULLLLLLU"
print(solution(dirs))