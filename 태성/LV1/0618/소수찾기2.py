n = 5

def solution(n):
    # 배수 확인 리스트
    check = [0] * (n+1)
    # 소수 리스트
    prime = []
    for x in range(2, n+1):
        # x가 소수
        if check[x] == 0:
            # 소수 리스트 추가
            prime.append(x)
            # x의 배수 체크
            for y in range(x, n+1, x):
                check[y] = 1
    # 소수 개수
    answer = len(prime)
    return answer

print(solution(n))