def tri(x):
    if x < 3:
        return x
    else:
        return tri(x // 3) * 10 + x % 3

def solution(n):
    answer = 0
    # 10진법 -> 3진법
    t = str(tri(n))
    # 앞뒤 반전 -> 10진법
    # 앞에서부터 3^i씩 곱하기와 동일
    for i in range(len(t)):
        answer += int(t[i]) * 3 ** (i)
    return answer