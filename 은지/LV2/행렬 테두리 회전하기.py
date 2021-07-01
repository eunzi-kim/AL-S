# 회전 함수
def rotation(info, m, min_v):
    r1 = info[0]-1
    c1 = info[1]-1
    r2 = info[2]-1
    c2 = info[3]-1
    # →
    for i in range(c1, c2):
        v = m[r1][i].pop(0)
        m[r1][i+1].append(v)
        if min_v > v:
            min_v = v
    # ↓
    for i in range(r1, r2):
        v = m[i][c2].pop(0)
        m[i+1][c2].append(v)
        if min_v > v:
            min_v = v
    # ←
    for i in range(c2, c1, -1):
        v = m[r2][i].pop(0)
        m[r2][i-1].append(v)
        if min_v > v:
            min_v = v
    # ↑
    for i in range(r2, r1, -1):
        v = m[i][c1].pop(0)
        m[i-1][c1].append(v)
        if min_v > v:
            min_v = v
    return min_v

def solution(rows, columns, queries):
    answer = []
    # 행렬 정보
    matrix = [[[x] for x in range(1, columns+1)]]
    for i in range(1, rows):
        matrix.append([[x] for x in range(columns*i+1, columns*i+columns+1)])
    print(matrix)
    # 쿼리들 돌리기
    for q in queries:
        # 가장 작은 값 결과 리스트에 추가
        answer.append(rotation(q, matrix, rows*columns))
    return answer