from itertools import combinations

def solution(relation):
    answer = 0
    result_arr = []
    N = len(relation)
    M = len(relation[0])
    for i in range(1, N+1):
        comb_arr = combinations(range(M), i)
        for j in comb_arr:
            is_break = False
            for result in result_arr:
                temp = len(result)
                for l in result:
                    for k in j:
                        if l == k:
                            temp -= 1
                        
                if temp == 0:
                    is_break = True
                    break

            if is_break: continue

            dict_arr = []
            for tuple in relation:
                temp = ''

                for k in j:
                    temp += tuple[k]
    
                if temp not in dict_arr:
                    dict_arr.append(temp)
                else:
                    break
        
            if len(dict_arr) == N:
                result_arr.append(list(j))
                answer += 1

    return answer

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
solution(relation)