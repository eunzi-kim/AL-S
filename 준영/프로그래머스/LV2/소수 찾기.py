from itertools import permutations

def is_prime(n):
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    arr = []
    numbers = list(numbers)
    for i in range(1, len(numbers)+1):
        temp = permutations(numbers, i)
        for j in temp:
            temp_n = int(''.join(j))
            if temp_n == 1 or temp_n == 0:
                continue
            if is_prime(temp_n):
                if temp_n not in arr:
                    arr.append(temp_n)
    answer = len(arr)
    return answer

solution("17")