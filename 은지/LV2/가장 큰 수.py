def solution(numbers):
    answer = ''
    num = [str(x)*3 for x in numbers]
    num.sort(reverse=True)
    for x in num:
        answer += x[:len(x)//3]
    answer = str(int(answer))
    return answer

numbers = [0, 0, 0]
print(solution(numbers))