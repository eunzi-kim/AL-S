def solution(d, budget):
    answer = 0
    # 오름차순 정렬
    d.sort()
    for x in d:
        # 예산이 부족한 경우 가지치기
        if budget < x:
            break
        # 예산 사용 가능
        else:
            budget -= x
            answer += 1
    return answer