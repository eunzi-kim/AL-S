def solution(info, query):
    answer = []
    person = []
    for v in info:
        person.append(v.split())
    
    for v in query:
        cnt_j = [x for x in range(len(person))]
        x = v.split()

        for i in range(4):
            k = 0
            while k < len(cnt_j):
                if (person[cnt_j[k]][i] != x[2*i]) and (x[2*i] != "-"):
                    cnt_j.pop(k)
                else:
                    k += 1

        l = 0
        while l < len(cnt_j):
            if (int(person[cnt_j[l]][4]) < int(x[7])) and (x[7] != "-"):
                cnt_j.pop(l)
            else:
                l += 1
            
        answer.append(len(cnt_j))
    return answer

i = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
q = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(i, q))