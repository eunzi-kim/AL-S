import itertools

def solution(relation):
    n = len(relation[0])
    m = len(relation)

    # 가능한 종류들의 모든 경우의 수 (인덱스)
    case = []
    for i in range(1, n+1):
        for v in itertools.combinations(range(n), i):
                case.append(v)
    
    i = 0
    while i < len(case):
        v = case[i]

        chk = []
        for k in range(m):
            # 종류 한 세트
            sub_c = []
            for j in v:                
                sub_c.append(relation[k][j])
            # 없는 세트이면 추가
            if sub_c not in chk:
                chk.append(sub_c)

        # 종류들이 모두 유일한 경우
        if len(chk) == m:
            # 이 종류 포함하는 경우들 없애기
            k = i+1
            while k < len(case):
                cnt = 0
                for w in case[i]:
                    if w in case[k]:
                        cnt += 1
                
                if cnt == len(case[i]):
                    case.pop(k)
                else:
                    k += 1
            i += 1

        # 종류들이 유일하지 않으면 없애기
        else:
            case.pop(i)
    
    return len(case)

relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
print(solution(relation))