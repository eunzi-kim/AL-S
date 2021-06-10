n = 3

# 3진법 만드는 함수
def mk_3(n):
    result = []
    # n >3으로 실수 했다가 찾음 ㅠ
    while n >= 3:
        result.append(n % 3)
        n = n // 3
    result.append(n)
    result.reverse()
    return result

# 10진법 만드는 함수
def mk_10(array):
    result = 0
    for i in range(len(array)):
        result += array[i]*(3**i)

    return result


def solution(n):

    answer = mk_10(mk_3(n))

    return answer

print(mk_3(n))

print(mk_10(mk_3(n)))

print(solution(n))