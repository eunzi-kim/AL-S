def solution(brown, yellow):
    answer = []
    total = brown + yellow
    idx = total
    while idx > 0:
        if total % idx == 0:
            x = (total // idx)
            y = idx
            if x * y == total and (x + y)*2 - 4 == brown:
                answer.append(y)
                answer.append(x)
                break
        idx -= 1
            
    return answer