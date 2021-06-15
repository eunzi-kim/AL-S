def solution(dartResult):
    # 점수 리스트
    score = []
    # 숫자 점수 
    subS = ''
    for x in dartResult:
        # 숫자 점수를 문자열 => 숫자 변경
        if len(subS) > 0:
            subV = int(subS)
        # 스타상
        if x == "*":
            if len(score) > 1:
                v1 = score.pop(-2)
                v2 = score.pop(-1)
                v1 *= 2
                score.append(v1)
                v2 *= 2
                score.append(v2)
            elif len(score) == 1:
                v1 = score.pop(-1)
                v1 *= 2
                score.append(v1)
        # 아차상
        elif x == "#":
            v = score.pop(-1)
            v *= -1
            score.append(v)
        # Single, Double, Triple
        elif x == 'S' or x == 'D' or x == "T":
            if x == 'S':
                subV **= 1
            elif x == 'D':
                subV **= 2
            elif x == 'T':
                subV **= 3
            score.append(subV)
            subS = ''
            subV = 0
        # 숫자 입력
        else:
            subS += x
    # 모든 점수의 합
    answer = sum(score)
    return answer