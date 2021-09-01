# 10진수 => 2진수
def two(x):
    if x < 2:
        return x
    else:
        return x % 2 + two(x//2)*10

def solution(s):
    zero = cnt = 0
    # s가 1이 되면 끝!
    while s != "1":
        # 반복 횟수
        cnt += 1
        # 0 개수
        zero += s.count("0")
        # 1의 개수를 이진수로 변경
        s = str(two(s.count("1")))
    answer = [cnt, zero]
    return answer