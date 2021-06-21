def solution(n):
    arr = list(str(n))
    arr.sort(reverse=True)
    answer = int(''.join(arr))
    return answer
print(solution(118372))
