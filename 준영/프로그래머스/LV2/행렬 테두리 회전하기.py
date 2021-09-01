def solution(rows, columns, queries):
    answer = []
    init_arr = [[0 for _ in range(columns)] for _ in range(rows)]

    for i in range(1, rows+1):
        for j in range(1, columns+1):
            init_arr[i-1][j-1] = (i-1)*columns + j

    for query in queries:
        temp = [[0 for _ in range(columns)] for _ in range(rows)]
        arr = []
        start_x = query[0]
        start_y = query[1]
        end_x = query[2]
        end_y = query[3]

        for j in range(start_y, end_y):
            temp[start_x-1][j] = init_arr[start_x-1][j-1]
            arr.append(temp[start_x-1][j])

        for i in range(start_x, end_x):
            temp[i][end_y-1] = init_arr[i-1][end_y-1]
            arr.append(temp[i][end_y-1])

        for j in range(start_y, end_y):
            temp[end_x-1][j-1] = init_arr[end_x-1][j]
            arr.append(temp[end_x-1][j-1])

        for i in range(start_x, end_x):
            temp[i-1][start_y-1] = init_arr[i][start_y-1]
            arr.append(temp[i-1][start_y-1])

        for i in range(rows):
            for j in range(columns):
                if temp[i][j] != 0:
                    init_arr[i][j] = temp[i][j]
        
        answer.append(min(arr))

    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))
rows = 3
columns = 3
queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]	
print(solution(rows, columns, queries))
rows = 100
columns = 97
queries = [[1,1,100,97]]	
print(solution(rows, columns, queries))