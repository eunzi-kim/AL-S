def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True, key=lambda x: x*10)
    answer = ''.join(numbers)
    answer = str(int(answer))
    return answer

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))