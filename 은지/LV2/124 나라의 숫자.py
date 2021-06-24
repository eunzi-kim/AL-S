def solution(n):
    R = []
    # 3씩 뛰어가는 규칙 이용
    while n > 0:
        if n % 3 == 1:
            R.append('1')
            n //= 3
        elif n % 3 == 2:
            R.append('2')
            n //= 3
        else:
            R.append('4')
            n = n // 3 - 1
    # 배열 역방향 후 문자열로 변경
    answer = ''.join(R[::-1])
    return answer

n = 6
print(solution(n))