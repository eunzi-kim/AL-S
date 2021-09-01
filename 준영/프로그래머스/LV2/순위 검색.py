def solution(info, query):
    answer = [0] * len(query)
    
    arr = []
    for i in info:
        arr.append(i.split())
    
    query_set = []
    for q in query:
        temp = q.split(' and ')
        t = temp.pop()
        x, y = t.split()
        temp.append(x) 
        temp.append(y)
        query_set.append(temp)

    for i in range(len(query_set)):
        arr_bool = [True] * len(arr)
        for j in range(len(query_set[i])-1):
            if query_set[i][j] == '-':
                continue
            for k in range(len(arr)):
                if query_set[i][j] != arr[k][j]:
                    arr_bool[k] = False
            
        for k in range(len(arr)):
            if int(query_set[i][-1]) > int(arr[k][-1]):

                arr_bool[k] = False

        answer[i] = arr_bool.count(True)

    return answer

info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

solution(info, query)