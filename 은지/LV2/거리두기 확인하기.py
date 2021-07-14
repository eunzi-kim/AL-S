def solution(places):
    answer = []
    for p in places:
        person = []
        for i in range(5):
            for j in range(5):
                if p[i][j] == "P":
                    person.append((i, j))
        
        cnt = 1
        for i in range(len(person)-1):
            for j in range(i+1, len(person)):
                r1 = person[i][0]
                r2 = person[j][0]
                c1 = person[i][1]
                c2 = person[j][1]
                if r1 == r2:
                    if abs(c1-c2) == 1:
                        cnt = 0
                        break
                    elif abs(c1-c2) == 2:
                        if p[r1][(c1+c2)//2] != "X":
                            cnt = 0
                            break
                elif c1 == c2:
                    if abs(r1-r2) == 1:
                        cnt = 0
                        break
                    elif abs(r1-r2) == 2:
                        if p[(r1+r2)//2][c1] != "X":
                            cnt = 0
                            break
                # 대각선 확인
                else:
                    if abs(r1-r2) == 1 and abs(c1-c2) == 1:
                        if p[r1][c2] != "X" or p[r2][c1] != "X":
                            cnt = 0
                            break

        if cnt:
            answer.append(1)
        else:
            answer.append(0)
    return answer