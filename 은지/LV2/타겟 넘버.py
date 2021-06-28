answer = 0

def add(i, sumV, numbers, target):
    global answer

    if i == len(numbers):
        if sumV == target:
            answer += 1
    else:
        add(i+1, sumV+numbers[i], numbers, target)
        add(i+1, sumV-numbers[i], numbers, target)


def solution(numbers, target):
    add(0, 0, numbers, target)
    return answer

numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))