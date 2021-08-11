def solution(dirs):
    answer = 0

    dict = []

    now = [0, 0]
    for i in dirs:
        temp1 = now[:]
        if i == 'U':
            now[1] += 1
            if now[1] > 5:
                now[1] -= 1
                continue
        elif i == 'D':
            now[1] -= 1
            if now[1] < -5:
                now[1] += 1
                continue
        elif i == 'L':
            now[0] -= 1
            if now[0] < -5:
                now[0] += 1
                continue
        elif i == 'R':
            now[0] += 1
            if now[0] > 5:
                now[0] -= 1
                continue
        temp2 = now[:]
        path = str(temp1[0])+str(temp1[1])+str(temp2[0])+str(temp2[1])
        path2 = str(temp2[0])+str(temp2[1])+str(temp1[0])+str(temp1[1])

        if path not in dict and path2 not in dict:
            dict.append(path)
            dict.append(path2)
            answer += 1
        
    return answer

dirs = 'ULURRDLLU'
solution(dirs)