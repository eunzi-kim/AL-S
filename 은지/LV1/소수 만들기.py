from itertools import combinations

def solution(nums):
    answer = 0
    # 소수 리스트
    prime = [2]
    # 가장 크게 나올 수 있는 숫자
    M = max(nums) * 3
    Chk = [1] * (M+1)
    # 소수 구하기
    for x in range(3, M+1, 2):
        if Chk[x]:
            prime.append(x)
            for y in range(x, M+1, x):
                Chk[y] = 0

    # 주어진 숫자 3개 조합
    C = list(combinations(nums, 3))
    # 주어진 숫자 중 3개의 수를 더하기
    for c in C:
        # 소수가 되는 경우
        if sum(c) in prime:
            answer += 1
    return answer