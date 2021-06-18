arr = [5, 9, 7, 10]

divisor = 5

def solution(arr, divisor):
    answer = []

    for a in arr:
        if a % divisor == 0:
            answer.append(a)

    if len(answer) == 0:
        answer.append(-1)

    answer = sorted(answer)
    return answer

print(solution(arr, divisor))