def two(x):
    if x < 2:
        return x
    else:
        return x % 2 + two(x//2) * 10

def solution(n):
    answer = 0
    two_n = str(two(n))
    m = two_n.count("1")
    for x in range(n+1, 1000001):
        if str(two(x)).count("1") == m:
            answer = x
            break
    return answer

n = 78
print(solution(n))