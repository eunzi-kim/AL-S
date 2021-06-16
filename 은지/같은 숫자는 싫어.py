def solution(arr):
    answer = []
    # 과거 숫자 초기화
    pre = -1
    for x in arr:
        # 과거 숫자와 현재 숫자 다른 경우
        if pre != x:
            answer.append(x)
            # 과거 숫자 변경
            pre = x
    return answer